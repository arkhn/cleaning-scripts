import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"


class GithubConfig(object):
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if GITHUB_TOKEN is None:
        raise RuntimeError(
            "Please provide .env file with your GitHub token: GITHUB_TOKEN='...'.\n"
            "This file should be in the app/ package."
        )

    CLONE_PATH = "/tmp/clones"
    ORGA = "Arkhn"
    REPO = "cleaning-scripts"
