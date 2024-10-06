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

class Word(BaseModel):
    word: str

class Card(BaseModel):
    id_card: int
    word: Word
    type: CardType

class GameModel(BaseModel):
    id_gamemodel: int
    id_user: int
    matrix: List[List[Card]]
    creation_date: datetime.date

class Game(BaseModel):
    id_user: int
    id_gamemodel: int
    nb_rounds: int
    date: datetime.date