from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from decouple import config
from fastapi import APIRouter

Base = automap_base()

engine = create_engine(config("DATABASE_URL"))

Base.prepare(engine, reflect=True)

SessionLocal = sessionmaker(bind=engine)

api = APIRouter()

def get_db():
    """Returns a new session to the database"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Refers the users table in db (with fields - id, name, email & password)
user = Base.classes.users

