#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """
    This is the class for user
    Attributes:
        __tablename__ (str): The table name  to store the users
        email (sqlalchemy String): The email address
        password (sqlalchemy String): The password
        first_name (sqlalchemy String): The first name
        last_name (sqlalchemy String): The last name
        places (sqlalchemy relationship): The User-Place relationship
        reviews (sqlalchemy relationship): The User-Review relationship
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
