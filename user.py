from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()


# Add new user
@route.post("/users")
def add_book(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User (name = request.name,
                           birthday =  request.birthday,
                           gender = request.gender,
                           email = request.email
                        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Retrieve a list of all users:

@route.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
# Retrieve details for a specific user:



@route.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return "User not found" 
    return user

# Update an existing user:
@route.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.User, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return "User not found"
    for var, value in vars(user_update).items():
        setattr(user, var, value) if value else None
    db.commit()
    return user

# delete an existing user:

@route.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return "User not found"
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}