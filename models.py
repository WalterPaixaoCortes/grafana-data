from sqlalchemy import (
    Column, String, Integer, DateTime, func, Sequence, Float, and_, Boolean, Text)
from marshmallow import ValidationError, pre_load, post_load
from database import Base


class IMDBMovies(Base):
    '''Model class for coverage table'''

    __tablename__ = 'imdb_movies'

    imdb_title_id = Column(String(255), primary_key=True)
    title = Column(String(255), nullable=True)
    original_title = Column(String(255), nullable=True)
    year = Column(Integer(), nullable=True)
    date_published = Column(DateTime(), nullable=True)
    genre = Column(String(255), nullable=True)
    duration = Column(Integer(), nullable=True)
    country = Column(String(255), nullable=True)
    language = Column(String(255), nullable=True)
    director = Column(String(255), nullable=True)
    writer = Column(String(255), nullable=True)
    production_company = Column(String(255), nullable=True)
    actors = Column(Text(), nullable=True)
    description = Column(Text(), nullable=True)
    avg_vote = Column(Float(), nullable=True)
    votes = Column(Integer(), nullable=True)
    budget = Column(Float(), nullable=True)
    usa_gross_income = Column(Float(), nullable=True)
    worlwide_gross_income = Column(Float(), nullable=True)
    metascore = Column(Float(), nullable=True)
    reviews_from_users = Column(Float(), nullable=True)
    reviews_from_critics = Column(Float(), nullable=True)


class IMDBNames(Base):
    __tablename__ = 'imdb_names'
    imdb_name_id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=True)
    birth_name = Column(String(255), nullable=True)
    height = Column(String(255), nullable=True)
    bio = Column(String(255), nullable=True)
    birth_details = Column(String(255), nullable=True)
    date_of_birth = Column(String(255), nullable=True)
    place_of_birth = Column(String(255), nullable=True)
    death_details = Column(String(255), nullable=True)
    date_of_death = Column(String(255), nullable=True)
    place_of_death = Column(String(255), nullable=True)
    reason_of_death = Column(String(255), nullable=True)
    spouses_string = Column(String(255), nullable=True)
    spouses = Column(String(255), nullable=True)
    divorces = Column(String(255), nullable=True)
    spouses_with_children = Column(String(255), nullable=True)
    children = Column(String(255), nullable=True)
