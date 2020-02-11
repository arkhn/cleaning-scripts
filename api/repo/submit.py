from api.repo.pull_request import new_pull_request
from api.repo.issue import new_issue


def submit(name, description, code, input, output):

    examples = [(input, output)]

    new_issue(name, description, code, examples)

    branch_name = new_pull_request(name, description, code, examples)

    return branch_name
