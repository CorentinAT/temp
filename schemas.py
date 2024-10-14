from typing import List
from pydantic import BaseModel
import datetime
from enum import Enum

class CardType(str, Enum):
    KEYCARD = "KEYCARD"
    AGENTCARD = "AGENTCARD"
    ASSASSINGCARD = "ASSASSINGCARD"

class User(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    hashed_password: str

class Word(BaseModel):
    word: str

class GameModel(BaseModel):
    id_user: int
    creation_date: datetime.date

class Card(BaseModel):
    id_card: int
    word: Word
    type: CardType
    gamemodel: GameModel

class Game(BaseModel):
    id_user: int
    id_gamemodel: int
    nb_rounds: int

class Association(BaseModel):
    id_gamemodel: int
    key_word: str