from flask import render_template, flash, redirect, request, url_for

from app import app
from app.forms import NewScriptForm

from app.repo.submit import submit
from app.repo.check import get_branch_status


@app.route("/new", methods=["GET", "POST"])
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
        return redirect(url_for("check", branch=branch_name))

    return render_template("new_script.html", title="Add a new script", form=form)


@app.route("/check")
def check():
    branch_name = request.args.get("branch", None)
    status, color = get_branch_status("cleaning-scripts", branch_name)

    print("STATUS:", branch_name)
    print(status)
    return render_template(
        "check.html", title="Home", branch_name=branch_name, status=status, color=color
    )


@app.route("/")
@app.route("/index")
def index():
    print(get_branch_status("cleaning-scripts", "master"))
    return render_template("index.html", title="Home")
