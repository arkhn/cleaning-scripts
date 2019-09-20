import git
import os


def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def ensure_repo_exists(path, github_organization, github_repo):
    ensure_path_exists(path)

    repo_path = f"{path}/{github_repo}"

    if not os.path.isdir(repo_path):
        print("Cloning repo...")
        git.Git(path).clone(
            f"https://github.com/{github_organization}/{github_repo}.git"
        )
