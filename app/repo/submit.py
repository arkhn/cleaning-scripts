from app.github.pull_request import new_pull_request
from app.github.issue import new_issue
from app.github.check import get_branch_status


def submit(name, description, code, input, output):

    examples = [(input, output)]

    new_issue(name, description, code, examples)

    commit_sha = new_pull_request(name, description, code, examples)

    print(commit_sha)

    #print(get_branch_status("cleaning-scripts", "user1_new_branch"))