from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired(message="Name is required")])
    species = SelectField('Species')
    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    age = IntegerField('Age in Years', validators=[NumberRange(min=0, max=30, message='Please enter a number from 0 to 30')])
    notes = StringField('Add details about personality and temperament')