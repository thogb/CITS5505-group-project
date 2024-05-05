from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import EmailField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ProfileForm(FlaskForm):
    email = EmailField('Email')
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2 ,max=40)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=40)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=100)])
    city = SelectField('City', validators=[DataRequired()])
    submit = SubmitField('Save')