#!/usr/bin/env python3
"""User Model - SQLAlchemy ORM"""
from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """Implements the user"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, *args, **kwargs):
        """Init with super"""
        super.__init__(*args, kwargs)
