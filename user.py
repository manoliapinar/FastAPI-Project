from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()


# Add new user

# Retrieve a list of all users:

# Retrieve details for a specific user:

# Update an existing user:

# delete an existing user:
