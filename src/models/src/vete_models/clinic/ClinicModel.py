import inject

from vete_models.db import Sessions
from vete_entities.clinic.patient import Patient


class ClinicModel:

    @inject.autoparams()
    def __init__(self, sessions: Sessions):
        self.sessions = sessions

    def patients(self):
        with self.sessions.get() as session:
            patients = session.query(Patient).all()
            return patients
