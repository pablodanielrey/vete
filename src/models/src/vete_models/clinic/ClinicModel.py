import inject

from vete_models.db import Sessions
from vete_entities.clinic.animals import Species, Breed
from vete_entities.clinic.patient import Patient


class ClinicModel:

    @inject.autoparams()
    def __init__(self, sessions: Sessions):
        self.sessions = sessions


    def create_entities(self):
        from vete_entities.clinic.animals import get_breeds, get_species
        with self.sessions.get() as session:
            for s in get_species():
                if session.query(Species).filter(Species.id == s.id).count() <= 0:
                    session.add(s)
            session.commit()

            for b in get_breeds():
                if session.query(Breed).filter(Breed.id == s.id).count() <= 0:
                    session.add(b)
            session.commit()
    

    def patients(self):
        with self.sessions.get() as session:
            patients = session.query(Patient).all()
            return patients

    def add_patient(self, patient: Patient):
        with self.sessions.get() as session:
            session.add(patient)
            session.commit()

    def breeds_by_species(self, specie_id: str):
        with self.sessions.get() as session:
            r = session.query(Breed).filter(Breed.species_id == specie_id).all()
            return r

    def species(self):
        with self.sessions.get() as session:
            return session.query(Species).all()