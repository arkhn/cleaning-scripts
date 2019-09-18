"""Check that the PR passes tests"""
#
# # or using an access token
# g = Github("4b9f84ffb90209112049b635fc451a94dbf3bad5")

import requests
import json

headers = {
    'User-Agent': "MyClient/1.0.0",
    'Accept': "application/vnd.travis-ci.2.1+json",
    'Cache-Control': "no-cache",
    'Host': "api.travis-ci.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }


def get_branch_status(repo, branch):
    url = f"https://api.travis-ci.com/repos/arkhn/{repo}/branches/{branch}"
    response = requests.request("GET", url, headers=headers)

    response = json.loads(response.text)

    return response["branch"]["state"]
