from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    discord_id = Column(String, nullable=True)
    role = Column(String, default='contestant')

class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(DateTime)
    type = Column(String)
    max_teams = Column(Integer)
    players_per_team = Column(Integer)

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer)
    winner = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
