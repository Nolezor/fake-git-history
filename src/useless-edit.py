import requests
import subprocess
import os

def get_quote_of_the_day():
    try:
        response = requests.get('https://zenquotes.io/api/random/')
        if response.status_code == 200:
            quote_data = response.json()[0]
            quote = quote_data['q']
            author = quote_data['a']
            return quote, author
        else:
            print(f"Failed to fetch quote. Status code: {response.status_code}")
            return f"Status {response.status_code}", "Cthulhu"
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return "Cthulhu has swallowed the internet", "The Devourer of Sanity"

def update_file(quote, author):
    file_path = os.path.join(os.getcwd(), 'quotes.txt')
    with open(file_path, 'a') as f:
        f.write(f'# "{quote}" - {author}\n')

def git_commit_quote(author):
    try:
        # Stage the changes
        subprocess.run(['git', 'add', 'quotes.txt'], check=True, cwd=os.path.dirname(__file__))
        
        # Commit with author name as commit message
        subprocess.run(['git', 'commit', '-m', f'Quote by {author}'], check=True, cwd=os.path.dirname(__file__))
        
        print(f"Successfully committed quote by {author}")
    except subprocess.CalledProcessError as e:
        print(f"Git commit failed: {e}")

def main():
    quote, author = get_quote_of_the_day()
    if quote and author:
        update_file(quote, author)
        git_commit_quote(author)

if __name__ == '__main__':
    main()
