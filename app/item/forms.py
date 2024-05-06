from flask_wtf import FlaskForm
from wtforms import BooleanField, DecimalField, SelectField, StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileRequired, MultipleFileField, FileAllowed, FileSize

from app.services.category import checkIfCategoryExists
from app.services.city import checkIfCityExists

class BaseItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    city = SelectField('City', coerce=int, validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    used = BooleanField('Used', default=False)
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=500)])
    photos = MultipleFileField('Photos', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!'), FileSize(max_size=5 * 1024 * 1024)])

    def validate_city(self, city):
        if not checkIfCityExists(city.data):
            raise ValidationError('Invalid city')

    def validate_category(self, category):
        if not checkIfCategoryExists(category.data):
            raise ValidationError('Invalid category')

class NewItemForm(BaseItemForm):
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0.0, max=1000000.0)])

    submit = SubmitField('Submit')

class NewAuctionItemForm(BaseItemForm):
    start_price = DecimalField('Start Price', validators=[DataRequired(), NumberRange(min=0.0, max=1000000.0)])
    # TODO: Figure out the end time calculation

    submit = SubmitField('Submit')