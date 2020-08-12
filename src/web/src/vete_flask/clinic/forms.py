
import inject

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, HiddenField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

from vete_entities.clinic import Gender
from vete_entities.clinic.animals import Species, Breed

from vete_models.clinic import ClinicModel

def gender_choices():
    return [(i.value, i.name) for i in Gender]

class PatientForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    birth = DateField('Nacimiento')
    species = SelectField('Especie')
    gender = SelectField('Género', choices=gender_choices())
    breed = SelectField('Raza')
    color = StringField('Color')
    fur = StringField('Pelaje')
    blood_type = StringField('Factor')
    