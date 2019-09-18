"""Check that the PR passes tests"""
import requests
import json

from app.config import GithubConfig

github_organization = GithubConfig.ORGA

headers = {
    "User-Agent": "MyClient/1.0.0",
    "Accept": "application/vnd.travis-ci.2.1+json",
    "Cache-Control": "no-cache",
    "Host": "api.travis-ci.com",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "cache-control": "no-cache",
}


def get_branch_status(repo, branch):
    url = f"https://api.travis-ci.com/repos/{github_organization}/{repo}/branches/{branch}"
    response = requests.request("GET", url, headers=headers)

    response = json.loads(response.text)

    if "branch" in response:
        status = response["branch"]["state"]
        color_map = {
            "passed": "success",
            "pending": "warning",
            "failed": "danger",
            "errored": "danger",
            "canceled": "danger",
        }
        if status in color_map:
            color = color_map[status]
        else:
            color = "primary"
        return status, color
    else:
        return None, "primary"
