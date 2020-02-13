from flask import render_template, flash, redirect, request, url_for, jsonify, Blueprint
from flask_cors import CORS

from api.forms import NewScriptForm

from api.repo.submit import submit
from api.repo.check import get_branch_status
from api.repo.list import list_repo_scripts
from api.repo.show import show_repo_script

api = Blueprint("api", __name__)
# enable Cross-Origin Resource Sharing
# "Allow-Control-Allow-Origin" HTTP header
CORS(
    api,
    origins=[
        r"^https?://.*\.?arkhn\.org(?::\d+)?$",
        r"^https?://.*\.?arkhn\.com(?::\d+)?$",
        r"^https?://.*\.?ark\.hn(?::\d+)?$",
        r"^https?://localhost(?::\d+)?$",
        r"^https?://0.0.0.0(?::\d+)?$",
    ],
)


@api.route("/list")
def list_scripts():
    query = request.args.get("query", "")

    scripts = list_repo_scripts(query)

    if request.headers.get("Content-Type") == "application/json":
        return jsonify({"query": query, "scripts": scripts})
    else:
        return render_template(
            "list_scripts.html", title="Found scripts", scripts=scripts, query=query
        )


@api.route("/show/<script_name>")
def show_script(script_name):

    script = show_repo_script(script_name=script_name)

    if request.headers.get("Content-Type") == "application/json":
        return jsonify({"script": script})
    else:
        return render_template("show_script.html", title="Show script", script=script)


@api.route("/new", methods=["GET", "POST"])
def new_script():
    form = NewScriptForm()
    if form.validate_on_submit():
        branch_name = submit(
            form.name.data,
            form.description.data,
            form.code.data,
            form.input_value.data,
            form.output_value.data,
        )
        flash(f"Script submitted: {form.name.data}")
        return redirect(url_for("api.check", branch=branch_name))

    return render_template("new_script.html", title="Add a new script", form=form)


@api.route("/check")
def check():
    branch_name = request.args.get("branch", None)
    status, color = get_branch_status("cleaning-scripts", branch_name)

    if request.headers.get("Content-Type") == "application/json":
        return jsonify({"branch_name": branch_name, "status": status})
    else:
        return render_template(
            "check.html", title="Home", branch_name=branch_name, status=status, color=color
        )


@api.route("/")
@api.route("/index")
def index():
    return render_template("index.html", title="Home")
