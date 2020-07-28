import pytest

@pytest.fixture
def model():
    from vete.models.ClinicLogModel import ClinicLogModel
    model = ClinicLogModel()
    return model
