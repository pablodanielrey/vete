
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, DateField, SelectField
from wtforms.validators import DataRequired

from vete_entities.clinic.patient import Species


def sepecies_choices():
    return [(i.value, i.name) for i in Species]

class PatientForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    bird = DateField('Nacimiento')
    species = SelectField('Especie', choices=sepecies_choices())
    