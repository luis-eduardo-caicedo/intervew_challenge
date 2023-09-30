from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(256))
    last_name = Column(String(256))
    email = Column(String(256))
    password = Column(String(16))
    address_id = Column(Integer, ForeignKey('address.id'))

    address = relationship("Address", back_populates="user")


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address_1 = Column(String(256))
    address_2 = Column(String(256), nullable=True)
    city = Column(String(256))
    state = Column(String(256))
    zip = Column(Integer)
    country = Column(String(256))

    user = relationship("User", back_populates="address")
