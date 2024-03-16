import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))
    carachter_id = Column(Integer, ForeignKey("carachter.id"))
    planets_id = Column(Integer, ForeignKey("planets.id"))
    startships_id = Column(Integer, ForeignKey("starships.id"))



class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    age= Column(String(250), nullable=False)
    User_favorites = relationship(Favorites)


class Carachter(Base):
    __tablename__ = 'carachter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(Integer, primary_key=True)
    height= Column(Integer, primary_key=True)
    mass = Column(Integer, primary_key=True)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    birth_year= Column(String(250), nullable=False)
    Carachter_favorites = relationship(Favorites)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)
    population = Column(Integer, primary_key=True)
    climate = Column(String(250))
    orbital_period = Column(Integer, primary_key=True)
    rotation_period = Column(Integer, primary_key=True)
    diametro=  Column(Integer, primary_key=True)
    birth_year= Column(String(250), nullable=False)
    Planets_favorites = relationship(Favorites)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    const_in_credits = Column(String(250), nullable=False)
    Starships_favorites = relationship(Favorites) 



    
    
    
    


   
   
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
