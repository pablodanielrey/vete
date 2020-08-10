
from enum import Enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, or_, ForeignKey, Enum as SQLEnum

from vete_entities import Base

"""
class PaymentMethod(Enum):
    CASH = 'CASH'
    CARD = 'CARD'
    MERCADOPAGO = 'MERCADOPAGO'


class Payment(Base):

    __tablename__ = 'payments'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    deleted = Column(DateTime)

    date = Column(Date)
    time = Column(Time)

    person_id = Column(String, ForeignKey('persons.id'))
    payment_method_id = Column(String)
    method = Column(SQLEnum(PaymentMethod))
    ammount = Column(Float)
    concept = Column(String)
"""

