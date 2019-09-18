from github import Github
import requests

# First create a Github instance:

hostname = "github.com/arkhn"

# or using an access token
g = Github("4b9f84ffb90209112049b635fc451a94dbf3bad5")

# Github Enterprise with custom hostname
repo = g.get_repo("arkhn/cleaning-scripts")

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
        self.title = "Why are you requesting a new script?"
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
        self.content = "\n".join([
            f"{input} --> {output}"
            for input, output in examples
        ])


# TODO use template flask
def new_issue(script_name, description, code, examples):
    body = (
        f"#{script_name}\n\n" +
        str(Purpose(description)) +
        str(Script(code)) +
        str(Test(examples))
    )

    print(body)

    # repo.create_issue(
    #     title=title + script_name,
    #     labels=[new_label],
    #     body=body,
    # )
