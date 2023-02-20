from database.database import get_db,user
from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
import json

def read_user(id: int, db: Session = Depends(get_db)):

    data = db.query(user).filter(user.id == id).all()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

