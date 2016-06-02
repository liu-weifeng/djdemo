import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    admin = Column(bool, default=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    dep_id = Column(Integer, ForeignKey('department.id'), nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(float, nullable=False)


class Booking(Base):
    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    art_id = Column(Integer, ForeignKey('article.id'), nullable=False)
    num = Column(Integer, ForeignKey('article.id'), nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('mysql://djdemo:djdemo@127.0.0.1/djdemo')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
