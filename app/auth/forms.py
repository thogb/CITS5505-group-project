from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from app.models import User

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=40)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(max=255), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=40)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # def validate(self, extra_validators=None):
    #     fields_validate = super(RegisterForm, self).validate(extra_validators)

    #     if not fields_validate:
    #         return False

    #     # Find if email already registered
    #     user = User.query.filter_by(email=self.email.data).first()

    #     if user:
    #         return False

    #     return True