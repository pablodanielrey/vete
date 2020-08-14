import pytest
import uuid

def test_add_patient(model):
    from vete_entities.clinic.patient import Patient
    p = Patient()
    p.id = str(uuid.uuid4())
    p.name = 'pepito'
    
    model.add_patient(p)