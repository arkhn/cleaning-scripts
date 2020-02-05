"""List scripts"""
import re

from api.config import GithubConfig
from api.repo.utils import get_list_files


clone_path = GithubConfig.CLONE_PATH
github_organization = GithubConfig.ORGA
github_repo = GithubConfig.REPO
github_token = GithubConfig.GITHUB_TOKEN

REPO_PATH = f"{clone_path}/{github_repo}"


substitution_regex = r"def (\w+?)\("


def show_repo_script(script_name):

    script_files = get_list_files(REPO_PATH)

    for category, script_path, script_file in script_files:
        with open(f"{script_path}/{script_file}", "r") as content_file:
            content = content_file.read()

            script_func_name = re.search(substitution_regex, content)
            if script_func_name is not None:
                script_func_name = script_func_name.group(1)

            if script_name == script_func_name or script_file == f"{script_name}.py":

                results = re.search('"""(.*?)"""', content.replace("\n", " "))
                if results is not None:
                    description = results.group(1)
                else:
                    description = None

                return {
                    "category": category,
                    "name": script_name,
                    "description": description,
                    "code": content,
                    "test": "Tests are not available",
                }

    raise FileNotFoundError(f"The script {script_name} didn't match a script file.")
