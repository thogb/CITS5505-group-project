from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp

class ProfileForm(FlaskForm):
    email = EmailField('Email')
    # Retrieved from https://stackoverflow.com/questions/39990179/regex-for-australian-phone-number-validation#answer-56266834
    # The australia phone number regex is been used here
    # Date: 2024/05/05
    phone_number = StringField('Phone Number', validators=[DataRequired(),
                                                           Regexp(r'^(\+?\(61\)|\(\+?61\)|\+?61|\(0[1-9]\)|0[1-9])?( ?-?[0-9]){7,9}$', message="Invalid phone number"),
                                                            Length(max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2 ,max=40)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=40)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=100)])
    city = SelectField('City', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')

    # def validate_phone_number(self, phone_number):
    #     if not phone_number.data.startswith('+61'):
    #         raise ValidationError('Invalid phone number')