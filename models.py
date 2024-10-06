from sqlalchemy import JSON, Column, Integer, String, Date, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, unique=True)
    hashed_password = Column(String)

class Word(Base):
    __tablename__ = "words"
    word = Column(String, primary_key=True, unique=True)

class Card(Base):
    __tablename__ = "cards"
    id_card = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    word = Column(String, ForeignKey("words.word"))
    type = Column(String)

class GameModel(Base):
    __tablename__ = "gamemodels"
    id_gamemodel = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(Integer, ForeignKey("users.username"))
    matrix = Column(JSON)
    creation_date = Column(Date)

class Game(Base):
    __tablename__ = "games"
    id_game = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String, ForeignKey("users.username"))
    nb_rounds = Column(Integer)
    date = Column(Date)