"""List scripts"""
import git
import os
from os import listdir
from os.path import isfile, join
import re
import random

from app.config import GithubConfig


clone_path = GithubConfig.CLONE_PATH
github_organization = GithubConfig.ORGA
github_repo = GithubConfig.REPO
github_token = GithubConfig.GITHUB_TOKEN

REPO_PATH = f"{clone_path}/{github_repo}"

if not os.path.isdir(REPO_PATH):
    print("Cloning repo...")
    git.Git(clone_path).clone(
        f"https://github.com/{github_organization}/{github_repo}.git"
    )

repo = git.Repo(REPO_PATH)


def list_repo_scripts(query):
    repo.git.pull("--rebase")

    query = query.lower()
    script_path = f"{REPO_PATH}/scripts/custom"
    script_files = [f for f in listdir(script_path) if isfile(join(script_path, f)) and '__' not in f]
    print(script_files)
    scripts = []
    for script_file in script_files:
        with open(f"{script_path}/{script_file}", 'r') as content_file:
            content = content_file.read()

            results = re.search(r"def (\w+?)\(", content)
            if results is not None:
                script_name = results.group(1)
            else:
                script_name = f"{script_file} (looks broken)"

            content = content.replace('\n', ' ')
            results = re.search('"""(.*?)"""', content)
            if results is not None:
                description = results.group(1)
            else:
                description = f"(empty description)"

            print("query", query)
            if query == "" or query in script_name.lower() or query in description.lower():
                scripts.append((script_name, description))

    return scripts

