from fastapi import FastAPI
from pydantic import BaseModel
from database.dataset import pokemonDataBase
from schemas.pokemon import Pokemon
from routes.pokemon import router as pokemonRouter

from database.connection import engine
from database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pokemonRouter)

@app.get("/") 
def printHelloWorld():
    return {"message":"Pokemon App"}



