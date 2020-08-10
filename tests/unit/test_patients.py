
import pytest
import uuid

from vete_entities.clinic.patient import Patient

def test_add_patient(model):
    p = Patient()
    p.id = str(uuid.uuid4())
    p.name = 'pepito'

    model.add_patient(p)
