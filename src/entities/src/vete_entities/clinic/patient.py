import enum
from sqlalchemy import ForeignKey, Column, Integer, Float, String, DateTime, Text, Date, Enum

from vete_entities import Base
from . import Gender

Species = enum.Enum('Specie', ['CAT', 'DOG'])


class Patient(Base):

    __tablename__ = 'patients'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)
    name = Column(String)
    birth = Column(Date)

    species = Column(Enum(Species))
    gender = Column(Enum(Gender))

    breed = Column(String)
    color = Column(String)
    fur = Column(String)
    bood_type = Column(String)


class Castrated(Base):

    __tablename__ = 'castrated'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    date = Column(Date)
    description = Column(Text)
    patient_id = Column(String, ForeignKey('patients.id'))


class Vitals(Base):

    __tablename__ = 'vitals'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)
    temperature = Column(Float)
    weight = Column(Float)
    description = Column(String)

    patient_id = Column(String, ForeignKey('patients.id'))
