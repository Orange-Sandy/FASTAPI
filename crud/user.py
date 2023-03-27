from database.database import get_db,User
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

#Function to read all users in the user table in database
def read_all_user(db: Session = Depends(get_db)):
    Users = db.query(User).all()
    if not Users:
        raise HTTPException(status_code=404, detail="Data not found")
    return Users

#Function to read users in the user table in database with the ID
def read_user(id: int, db: Session = Depends(get_db)):
    """Read a user by id"""
    Users = db.query(User).filter(User.id == id).all()
    if not Users:
        raise HTTPException(status_code=404, detail="Data not found")
    return Users

#Function to add new users in the user table in database
def post_user(id:int,name:str,email:str,password:str, db: Session = Depends(get_db)):
    """Create a new user"""
    New_User = User(id=id,name=name,email=email,password=password)
    if not New_User:
        raise HTTPException(status_code=204, detail="Data not added")
    db.add(New_User)
    db.commit()
    db.refresh(New_User)
    return {"msg": "Data Added"}

#Function to update user data in the user table in database with the ID
def update_user(id:int,name:str, db: Session = Depends(get_db)):
    """Update a user"""
    User_to_update = db.query(User).filter(User.id == id).first()
    if not User_to_update:
        raise HTTPException(status_code=204, detail="Data not updated")
    User_to_update.id = id
    User_to_update.name = name
    db.commit()
    return {"msg": "Data Updated"}

#Function to dalete user data in the user table in database with the ID
def delete_user(id: int, db: Session = Depends(get_db)):
    """Delete a user"""
    user_to_delete = db.query(User).filter(User.id == id).first()
    if not user_to_delete:
        raise HTTPException(status_code=405, detail="Data not found")
    db.delete(user_to_delete)
    db.commit()
    return {"User Deleted"}