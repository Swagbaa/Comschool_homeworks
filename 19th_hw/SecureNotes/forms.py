from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from models import User


class RegisterForm(FlaskForm):
    username = StringField(
        "მომხმარებლის სახელი",
        validators=[DataRequired(), Length(min=3, max=80)],
    )
    password = PasswordField(
        "პაროლი", validators=[DataRequired(), Length(min=4, max=128)]
    )
    confirm_password = PasswordField(
        "გაიმეორეთ პაროლი",
        validators=[DataRequired(), EqualTo("password", message="პაროლები არ ემთხვევა")],
    )
    submit = SubmitField("რეგისტრაცია")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("ეს მომხმარებლის სახელი უკვე დაკავებულია.")


class LoginForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired()])
    submit = SubmitField("შესვლა")


class NoteForm(FlaskForm):
    title = StringField(
        "სათაური", validators=[DataRequired(), Length(min=1, max=150)]
    )
    content = TextAreaField("ტექსტი", validators=[DataRequired()])
    submit = SubmitField("შენახვა")