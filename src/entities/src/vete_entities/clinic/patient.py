import enum
from sqlalchemy import ForeignKey, Column, Integer, Float, String, DateTime, Text, Date, Enum

from vete_entities import Base
from . import Gender



class Patient(Base):

    __tablename__ = 'patients'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)
    name = Column(String)
    birth = Column(Date)
    gender = Column(Enum(Gender))
    color = Column(String)
    fur = Column(String)
    bood_type = Column(String)
    
    breed_id = Column(String, ForeignKey('breeds.id'), nullable=False)


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
