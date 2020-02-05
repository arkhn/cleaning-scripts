"""List scripts"""
import git
import os
import re

from api.config import GithubConfig
from api.repo.utils import get_list_files


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

substitution_regex = r"def (\w+?)\("


def list_repo_scripts(query):
    repo.git.pull("--rebase")

    query = query.lower()
    script_files = get_list_files(REPO_PATH)

    scripts = []
    for category, script_path, script_file in script_files:
        with open(f"{script_path}/{script_file}", "r") as content_file:
            content = content_file.read()

            results = re.search(substitution_regex, content)
            if results is not None:
                script_name = results.group(1)
            else:
                script_name = f"{script_file} (looks broken)"

            content = content.replace("\n", " ")
            results = re.search('"""(.*?)"""', content)
            if results is not None:
                description = results.group(1)
            else:
                description = None

            if (
                query == ""
                or query in script_name.lower()
                or query in description.lower()
            ):
                scripts.append(
                    {
                        "category": category,
                        "name": script_name,
                        "description": description,
                    }
                )

    return scripts
