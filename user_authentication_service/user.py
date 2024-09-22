#!/usr/bin/env python3
""" Module that contains a User class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class creation to map python classes to database tables
Base = declarative_base()

# Define a model that maps to a table
class User(Base):
    """ Class that saves the user data to a SQL table
    """

    # The name of the table in the database
    __tablename__ = 'users'

    # Save the user's data in the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
