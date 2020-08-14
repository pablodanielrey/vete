import pytest

@pytest.fixture(scope='module')
def prepare_dbs():
    import inject
    from vete_models.db import Sessions
    inject.configure_once()
    sessions = inject.instance(Sessions)
    sessions.generate_database()