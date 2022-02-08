### MODULE GIVEN BY CODEUP INSTRUCTORS
"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
from bs4 import BeautifulSoup
import re
from env import github_token, github_username
from  time import sleep

# TODO: Add more repositories to the `REPOS` list below.

def github_api_request(url: str, headers) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str, headers) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url, headers)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str, headers) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url, headers)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str, headers) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo, headers)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }

def scrape_github_data(REPOS, headers) -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo, headers) for repo in REPOS]

def get_repo_names(url, headers, page_num=14):
    ### in the above function definition, change page_num

    REPOS = []
    while page_num < 51:

        response = requests.get(url, headers=headers)
        print(page_num, response.status_code)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        links = soup.find_all("a", class_="v-align-middle")

        for link in links:
            name = link["href"]
            REPOS.append(name)
            with open("repo_names.txt", "a") as names:
                names.write(F"{name}\n")

        next_page = f"https://github.com{soup.find('a', class_='next_page')['href']}"
        page_num += 1
        url = re.sub(r"[0-9]", f"{page_num}", next_page)

        sleep(10)

    return REPOS

def main():

    headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

    if headers["Authorization"] == "token " or headers["User-Agent"] == "":
        raise Exception(
            "You need to follow the instructions marked TODO in this script before trying to use it"
        )

    ### in the url change the number
    # url = "https://github.com/search?p=14&q=nutrition&type=Repositories"
    # REPOS = get_repo_names(url, headers)

    with open("repo_names.txt", "r") as names:
        REPOS = names.readlines()
        REPOS = [name.replace("\n", "") for name in REPOS]

    data = scrape_github_data(REPOS, headers)
    json.dump(data, open("data.json", "w"), indent=1)

if __name__ == "__main__":
    main()