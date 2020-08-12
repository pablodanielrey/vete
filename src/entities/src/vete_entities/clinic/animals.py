import uuid
import datetime
import enum
from sqlalchemy import ForeignKey, Column, Integer, Float, String, DateTime, Text, Date, Enum

from vete_entities import Base


class Species(Base):
    __tablename__ = 'species'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)
    name = Column(String)



def get_species():
    return [
        Species(id='93a3e7ce-76b2-412c-a9f6-ee9cb9fc299d', created=datetime.datetime.utcnow(), name='Otro'),
        Species(id='3cec3fe9-052f-4a7d-8cb3-41da7263f6f7', created=datetime.datetime.utcnow(), name='Perro'),
        Species(id='811e4378-2016-43c3-9c32-af6cd856a2f7', created=datetime.datetime.utcnow(), name='Gato')
    ]

class Breed(Base):
    __tablename__ = 'breeds'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)
    name = Column(String)

    species_id = Column(String, ForeignKey('species.id'), nullable=False)


def get_breeds():
    return [
        Breed(id='93a3e7ce-76b2-412c-a9f6-ee9cb9fc299d', species_id='93a3e7ce-76b2-412c-a9f6-ee9cb9fc299d', created=datetime.datetime.utcnow(), name='Otro'),

        Breed(id='ce9ef979-231e-4cf4-b9e6-b73ae9cfeb89', species_id='3cec3fe9-052f-4a7d-8cb3-41da7263f6f7', created=datetime.datetime.utcnow(), name='Otro'),
        Breed(id='eb0b1655-2593-4858-baa1-e24befcb7704', species_id='3cec3fe9-052f-4a7d-8cb3-41da7263f6f7', created=datetime.datetime.utcnow(), name='Labrador'),
        Breed(id='f1070f27-1583-4014-8dca-e10ae4fdf045', species_id='3cec3fe9-052f-4a7d-8cb3-41da7263f6f7', created=datetime.datetime.utcnow(), name='Caniche'),
        Breed(id='e7122cb7-a257-4a63-8a9c-c22a0363ee9b', species_id='3cec3fe9-052f-4a7d-8cb3-41da7263f6f7', created=datetime.datetime.utcnow(), name='Dogo'),

        Breed(id='66a4c306-8d6f-4af7-beb9-62154491e178', species_id='811e4378-2016-43c3-9c32-af6cd856a2f7', created=datetime.datetime.utcnow(), name='Otro'),
        Breed(id='ec1acc98-e4e2-4f2c-a586-38f405e26f41', species_id='811e4378-2016-43c3-9c32-af6cd856a2f7', created=datetime.datetime.utcnow(), name='Egipcio'),
        Breed(id='355c3581-1f27-4927-b9fc-cfef7304dd40', species_id='811e4378-2016-43c3-9c32-af6cd856a2f7', created=datetime.datetime.utcnow(), name='Maycuun')
    ]
