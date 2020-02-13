"""Create and open an Issue"""
from github import Github
from api.config import GithubConfig


github_organization = GithubConfig.ORGA
github_repo = GithubConfig.REPO
github_token = GithubConfig.GITHUB_TOKEN

# Connect using an access token
g = Github(github_token)

repo = g.get_repo(f"{github_organization}/{github_repo}")

# make sure these labels exist on the repo
new_label = repo.get_label("new script")
update_label = repo.get_label("update script")

title = "New Script"


class Section:
    def __init__(self):
        self.title = ""
        self.content = ""

    def __str__(self):
        string = f"**{self.title}**"
        if self.content != "":
            string += f"\n{self.content}\n\n"
        return string


class Purpose(Section):
    def __init__(self, content):
        super().__init__()
        self.title = "What will the new script do?"
        self.content = content


class Script(Section):
    def __init__(self, content):
        super().__init__()
        self.title = "Describe your Python script below"
        self.content = f"```python\n{content}\n```"


class Test(Section):
    def __init__(self, examples):
        super().__init__()
        self.title = "Provide several expected inputs and outputs"
        self.content = "\n".join([f"`{input}` --> `{output}`" for input, output in examples])


# TODO use a template of flask instead
def new_issue(script_name, description, code, examples):
    issue_title = f"{title} {script_name}"
    body = (
        f"# {issue_title}\n\n" + str(Purpose(description)) + str(Script(code)) + str(Test(examples))
    )

    print(body)

    repo.create_issue(title=issue_title, labels=[new_label], body=body)
