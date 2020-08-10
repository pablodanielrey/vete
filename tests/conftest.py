import pytest
import inject

@pytest.fixture
def model():
    from vete_models.clinic.ClinicModel import ClinicModel
    model = inject.instance(ClinicModel)
    return model
