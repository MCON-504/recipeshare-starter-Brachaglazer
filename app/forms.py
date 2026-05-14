from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class FeedbackForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=120)]
    )
    topic = StringField(
        "Topic",
        validators=[DataRequired(), Length(max=100)]
    )
    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10, max=500)]
    )
    submit = SubmitField("Submit Feedback")

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

class ProfileForm(FlaskForm):
    display_name = StringField(
        "Display Name",
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    bio = TextAreaField(
        "Bio",
        validators=[Length(max=300)]
    )
    favorite_cuisine = StringField(
        "Favorite Cuisine",
        validators=[Length(max=80)]
    )
    years_cooking = IntegerField(
        "Years Cooking",
        validators=[Length(min=0, max=100)]
    )