from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField


class AddPetForm(FlaskForm):
    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = IntegerField('Age in Years')
    notes = StringField('Add details about personality and temperament')
    available = BooleanField('Available for adoption')