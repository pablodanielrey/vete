
from enum import Enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum

from vete_entities import Base


class CardType(Enum):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'


class Card(Base):

    __tablename__ = 'cards'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    person_id = Column(String, ForeignKey('persons.id'))
    type = Column(SQLEnum(CardTypes))
    number = Column(String)
    code = Column(String)
    brand = Column(String)


