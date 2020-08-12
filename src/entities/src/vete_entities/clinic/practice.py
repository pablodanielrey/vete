from sqlalchemy import ForeignKey, Column, Integer, Float, String, DateTime, Text, Date, Enum

from vete_entities import Base

from . import MedicationUnit


class Practice(Base):

    __tablename__ = 'practices'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    date = Column(Date)
    description = Column(Text)

    patient_id = Column(String, ForeignKey('patients.id'))


class MedApplication(Base):

    __tablename__ = 'med_applications'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    date = Column(Date)
    dose = Column(Float)
    unit = Column(Enum(MedicationUnit))
    medication = Column(String)
    description = Column(Text)

    practice_id = Column(String, ForeignKey('practices.id'))