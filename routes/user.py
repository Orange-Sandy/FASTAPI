from fastapi import APIRouter, Depends, Request,Response
import crud.user as init
from database.database import get_db,user,api
from sqlalchemy.orm import Session
import json
import time

@api.get("/id", tags=["User Details"])
def user(id:int, db: Session = Depends(get_db)):
    return init.read_user(id,db)