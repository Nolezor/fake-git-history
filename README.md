# GitHub Fake Commit History Generator

## 🌟 Project Overview

This script is a playful tool designed to generate random quotes and create artificial commit activity in your GitHub repository. It fetches a random quote from the Zenquotes API and adds it to a `quotes.txt` file, simulating consistent GitHub contribution activity.

## 🛠 Prerequisites

- Python 3.7+
- Git
- Internet connection

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/nolezor/fake-git-history.git
cd fake-git-history
```

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv .env
source .env/bin/activate  
# On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔧 Usage

Run the script manually:
```bash
python src/useless-edit.py
```

### Automated Usage

You can set up a cron job or GitHub Actions to run this script periodically:

#### Cron Job (Mac/Linux)
```bash
# Open crontab
crontab -e

# Add a line to run daily at midnight
0 0 * * * /path/to/your/python /path/to/GitHub-Fake-Commit-History/src/useless-edit.py
```

#### GitHub Actions (Recommended)
Create `.github/workflows/fake-commits.yml`:
```yaml
name: Generate Fake Commits
on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily at midnight
  workflow_dispatch:     # Allow manual triggering

jobs:
  generate-commits:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests
    - name: Run quote generator
      run: python src/useless-edit.py
```

## 🔍 How It Works

1. Fetches a random quote from Zenquotes API
2. Appends the quote to `quotes.txt`
3. Commits the changes to the repository

## 📋 Customization
- Modify `src/useless-edit.py` to change quote source or commit behavior
- Adjust GitHub Actions workflow for different scheduling

## ⚠️ Disclaimer

This script is for fun and demonstration purposes. Use responsibly and in compliance with GitHub's terms of service.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This repository is licensed under the GNU General Public License version 3 (GPLv3) as outlined in the [LICENSE](LICENSE) file.
