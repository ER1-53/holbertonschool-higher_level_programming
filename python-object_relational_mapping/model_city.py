#!/usr/bin/python3
"""Module city"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """class City"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
