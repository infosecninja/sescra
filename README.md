# GitHub Secrets Scraper (sescra.py)

**Created by Pramod Kumar**

This is a Python tool that allows you to search for a keyword in a GitHub repository's directories and files. It displays the 50 words before and after each occurrence of the keyword to provide context.

## Required Libraries

Before running the script, make sure to install the following required libraries:

- [requests](https://pypi.org/project/requests/): Used to make HTTP requests to the GitHub API.
- [tqdm](https://pypi.org/project/tqdm/): Used to display the progress bar while searching.

You can install these libraries using the following command:

```
pip install requests tqdm

```

## Usage

1. Install the required libraries (if not already installed):

2. Run the script `sescra.py`:

3. Follow the prompts:

- Enter the URL of the GitHub repository you want to search.
- Enter the keyword you want to search for.

The script will then search all directories and files for the keyword, and display 50 words before and after each occurrence as context.

If no password is found in the repository, the tool will inform you.

4. To quit the script, type `'exit'` when asked for the GitHub repository URL.

5. After each search, the tool will ask if you want to scan another repository or exit the script.

## Note

- This tool currently supports only public repositories, as it accesses the content via the GitHub API without any authentication.

- For private repositories, you will need to authenticate with GitHub using a personal access token or other appropriate methods.

- Please use this tool responsibly and only search for keywords in repositories that you have permission to access.

**Disclaimer**: The author is not responsible for any misuse of this tool or any actions taken based on the information provided by the tool.


