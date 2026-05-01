from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class RecipeForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired(), Length(min=3, max=80)]
    )
    description = StringField(
        "Description",
        validators=[DataRequired(), Length(max=120)]
    )
    instructions = PasswordField(
        "Instructions",
        validators=[DataRequired(), Length(min=8)]
    )
    prep_time = PasswordField(
        "Prep Time",
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit Recipe")
