from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import db, Base
from enums import PhoneType, ContactCategory


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(Enum(ContactCategory), nullable=False)

    phones = relationship("Phone", back_populates="contact", cascade="all, delete")


class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, nullable=False)
    type = Column(Enum(PhoneType), nullable=False)
    contact_id = Column(Integer, ForeignKey("contacts.id"))

    contact = relationship("Contact", back_populates="phones")
