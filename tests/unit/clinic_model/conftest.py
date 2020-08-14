import pytest

@pytest.fixture
def model(prepare_dbs):
    import inject
    from vete_models.clinic.ClinicModel import ClinicModel
    inject.configure_once()
    model = inject.instance(ClinicModel)
    return model