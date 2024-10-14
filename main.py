from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine
from .get_db import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

database = r"sql_app.db"

@app.post("/register/", response_model=schemas.UserResponse)
def create_user(
    user: schemas.User,
    db: Session = Depends(get_db)
):
    return crud.create_user(db=db, user=user)
