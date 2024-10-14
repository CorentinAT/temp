import schemas, models
from sqlalchemy import update, or_, func
from sqlalchemy.orm import Session
from get_db import get_db
from passlib.hash import sha256_crypt
from datetime import datetime, timedelta

def create_user(db:Session, user:schemas.User):
    hashed_password = sha256_crypt.hash(user.password)
    db_user = models.User(
        username = user.username,
        password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_gamemodel(db:Session, username):
    db_gamemodel = models.GameModel(
        id_user = username,
        creation_date = datetime.today().date()
    )
    db.add(db_gamemodel)
    db.commit()
    db.refresh(db_gamemodel)
    return db_gamemodel


def create_card(db: Session, card: schemas.Card) :
    db_card = models.Card(
        word = card.word,
        type = card.type,
        gamemodel = card.gamemodel
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def create_game(db: Session, game:schemas.Game) :
    db_game = models.Game(
        username = game.id_user,
        id_gamemodel = game.id_gamemodel,
        nb_rouds = game.nb_rounds,
        date = datetime.today().date()
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def create_association(db: Session, association: schemas.Association):
    db_association = models.Association(
        id_gamemodel = association.id_gamemodel,
        key_word = association.key_word,
    )
    db.add(db_association)
    db.commit()
    db.refresh(db_association)
    return db_association

def get_association_by_id(db:Session, id_association:int):
    return db.query(models.Association).filter(models.Association.id_association == id_association).first()

def get_user_by_id(db:Session, username:int):
    return db.query(models.User).filter(models.User.username == username).first()

def delete_association(db:Session, id_association:Int) :
    db_association: schemas.Association = get_association_by_id(db=db, id_association=id_association)
    db.delete(db_association)
    db.commit()
    return db_association

def delete_user_by_id(db, username:str):
    db_user: schemas.Association = get_user_by_id(db=db, username=username)
    db.delete(db_user)
    db.commit()
    return db_user
