# sescra.py
# Created by Pramod Kumar
# Github: https://github.com/infosecninja

import requests
import re
from tqdm import tqdm
import time

def get_github_repo_contents(repo_url, keyword):
    # Extract the repository owner and name from the repo URL
    owner, repo = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url).groups()

    # Get the repository contents using the GitHub API
    url = f'https://api.github.com/repos/{owner}/{repo}/contents'
    response = requests.get(url)

    if response.status_code == 200:
        repo_contents = response.json()

        # Get the total number of files to display the progress bar
        total_files = sum(item['type'] == 'file' for item in repo_contents)

        # Iterate through each directory and file in the repository
        for item in tqdm(repo_contents, desc="Searching files", unit="file", total=total_files):
            if 'type' in item:
                if item['type'] == 'dir':
                    # If the item is a directory, recursively call the function
                    get_github_repo_contents(item['url'], keyword)
                elif item['type'] == 'file':
                    # If the item is a file, fetch its content and search for the keyword
                    file_response = requests.get(item['download_url'])
                    if file_response.status_code == 200:
                        content = file_response.text
                        if search_keyword(keyword, content):
                            return True

    return False

def search_keyword(keyword, content):
    # Search for the keyword in the content using regular expressions
    pattern = re.compile(rf'(.{{0,50}}){re.escape(keyword)}(.{{0,50}})', re.IGNORECASE)
    matches = re.finditer(pattern, content)

    for match in matches:
        # Extract the context before and after the keyword
        context_before, _, context_after = match.groups()
        print("Found keyword:", keyword)
        print("Context Before:", context_before)
        print("Context After:", context_after)
        print('-' * 50)
        return True

    return False

def print_help():
    print("GitHub Secrets Scraper (sescra.py)")
    print("Created by Pramod Kumar")
    print("Usage:")
    print("1. Enter the URL of the GitHub repository you want to search.")
    print("2. Enter the keyword you want to search for.")
    print("The script will then search all directories and files for the keyword,")
    print("and display 50 words before and after each occurrence as context.")
    print()

if __name__ == "__main__":
    print_help()

    while True:
        repo_url = input("Enter the GitHub repository URL (or 'exit' to quit): ")
        if repo_url.lower() == 'exit':
            break

        keyword = input("Enter the keyword you want to search for: ")

        print("Searching for the keyword. Please wait...")
        time.sleep(1)  # Adding a short delay to show the progress bar smoothly

        if get_github_repo_contents(repo_url, keyword):
            print("Search completed.")
        else:
            print("No password found in the repository.")

        choice = input("Do you want to scan another repository? (yes/no): ")
        if choice.lower() != 'yes':
            break
