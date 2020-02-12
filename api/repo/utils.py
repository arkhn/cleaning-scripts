import git
import os
from os import listdir
from os.path import isfile, join


def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def ensure_repo_exists(path, github_organization, github_repo):
    ensure_path_exists(path)

    repo_path = f"{path}/{github_repo}"

    if not os.path.isdir(repo_path):
        print("Cloning repo...")
        git.Git(path).clone(f"https://github.com/{github_organization}/{github_repo}.git")


def get_list_files(REPO_PATH):
    categories = ["utils", "custom", "logic"]
    script_paths = [f"{REPO_PATH}/scripts/{category}" for category in categories]
    script_files = [
        (category, script_path, file)
        for category, script_path in zip(categories, script_paths)
        for file in listdir(script_path)
        if isfile(join(script_path, file)) and "__" not in file
    ]
    return script_files
