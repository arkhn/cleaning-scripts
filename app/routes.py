from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/new')
def new_script():
    form = LoginForm()
    return render_template('new_script.html', title="Add a new script", form=form)


@app.route('/submit')
def submit():
    return 'Noyimplketed'


@app.route('/test')
def test_script():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
