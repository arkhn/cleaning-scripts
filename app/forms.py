from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewScriptForm(FlaskForm):
    name = StringField('Nom du script', validators=[DataRequired()])
    code = TextAreaField('Code', validators=[DataRequired()])
    submit = SubmitField('Soumettre')