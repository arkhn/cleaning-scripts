"""Create and push a new branch"""
import git
import os
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


def create_pull_request(user, script_name, code):
    # Go in the proper branch
    branch_name = f"{user}_new_branch"
    print("CREATE branch", branch_name)
    new_branch = False
    try:
        repo.git.checkout(branch_name)
    except git.exc.GitCommandError:
        new_branch = True
        repo.git.checkout("HEAD", b=branch_name)

    # Write the code
    for file_name, file_content in code.items():

        if "test" in file_name:
            dir = "test/custom"
        else:
            dir = "scripts/custom"

        with open(f"{REPO_PATH}/{dir}/{file_name}", "w") as f:
            f.write(file_content)
            print("Write", file_name)

    repo.git.add("--all")
    repo.git.commit("-m", f"Add {script_name} script")

    if new_branch:
        repo.git.push("--set-upstream", "origin", branch_name)
    else:
        repo.git.push()

    commit_sha = repo.head.commit

    repo.git.checkout("master")

    return commit_sha, branch_name


def generate_test(script_code, examples):
    results = re.search("def (\w+?)\(", script_code)
    if results is not None:
        script_name = results.group(1)
        code = f"""
from scripts.custom import {script_name}

def test_{script_name}():
"""
        for input, output in examples:
            code += f"""
    output = {script_name}("{input}")
    assert output == "{output}"

"""
        return code
    else:
        raise ValueError("The script provided doesn't seem to be valid.")


def new_pull_request(script_name, description, script_code, examples):
    user = f"user{random.randint(10000, 100000)}"
    print(generate_test(script_code, examples))
    code = {
        f"script_{script_name}.py": script_code,
        f"test_script_{script_name}.py": generate_test(script_code, examples),
    }

    commit_sha, branch_name = create_pull_request(user, script_name, code)
    print(commit_sha)

    return branch_name
