from fastapi import Depends
import crud.user as init
from database.database import get_db,api
from sqlalchemy.orm import Session

@api.get("/user", tags=["User Details"])
def User(db: Session = Depends(get_db)):
    return init.read_all_user(db)

@api.get("/user/{id}", tags=["FETCH"])
def get(id: int, db: Session = Depends(get_db)):
    return init.read_user(id,db)

@api.post("/user/add", tags=["INSERT"])
def post(id:int, name:str,email:str,password:str, db: Session = Depends(get_db)):
    return init.post_user(id,name,email,password,db)

@api.put("/user/update/{id}", tags=["UPDATE"])
def put(id:int, name:str, db: Session = Depends(get_db)):
    return init.update_user(id,name,db)

@api.delete("/user/delete/{id}", tags=["DELETE"])
def delete(id:int, db: Session = Depends(get_db)):
    return init.delete_user(id,db)