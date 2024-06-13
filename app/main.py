from fastapi import FastAPI
from app.api import endpoints
from app.db import engine, Base


# Create the database tables
Base.metadata.create_all(bind=engine)



app = FastAPI()

# Define a simple route
@app.get("/")
def read_root():
    return {"Hello": "World"}  

# Include your CRUD routes
app.include_router(endpoints.router)
