from fastapi import FastAPI
import  models
from database import engine
import book, user

# Create an instance of FastAPI
app = FastAPI()

# Create table from models
models.Base.metadata.create_all(engine)

# Root endpoint
@app.get("/")
def root():
    return 'Welcome to ESG Data & IA FastAPI Workshop'

# Run book route
app.include_router(book.route)


# Run user route
app.include_router(user.route)