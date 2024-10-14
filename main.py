from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


