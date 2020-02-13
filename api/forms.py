from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewScriptForm(FlaskForm):
    name = StringField("Script name", validators=[DataRequired()])
    description = StringField(
        "Enter a short description of what the script does", validators=[DataRequired()]
    )
    code = TextAreaField("Write down here the code of the script", validators=[DataRequired()])

    input_value = StringField("Raw input", validators=[DataRequired()])
    output_value = StringField("Expected output", validators=[DataRequired()])

    submit = SubmitField("Submit the script for validation")
