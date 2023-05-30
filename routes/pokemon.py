from fastapi import APIRouter, Depends
from database.dataset import pokemonDataBase
from schemas.pokemon import Pokemon, PokemonResponseModel
from database.connection import get_db
from database.models import Pokemon as PokemonTableModel
from sqlalchemy.orm import Session
import operator

router = APIRouter(prefix="/pokemons", tags=["pokemons"])

@router.get ("/", response_model=list[PokemonResponseModel])
def getPokemons(db: Session =Depends(get_db)):
    pokemons = db.query(PokemonTableModel).all()
    return pokemons


@router.post("/")
def addPokemon (pokemon: Pokemon, db:Session= Depends(get_db)):
    pokemonData = PokemonTableModel(name=pokemon.name, type1=pokemon.type1, classification=pokemon.classification, type2=pokemon.type2, generation=pokemon.generation)
    db.add(pokemonData)
    db.commit()
    db.refresh(pokemonData)
    return {"data": pokemonData}

@router.get("/{pokemonName}")
def getSpecificPokemon(pokemonName: str, db: Session =Depends(get_db)):
    pokemon = db.query(PokemonTableModel).filter(PokemonTableModel.name.ilike(f"%{pokemonName}%")).first()
    if pokemon:
        return {"data": pokemon}
    return {"message": "Found Nothing"}

@router.delete("/{pokemonId}")
def deletePokemon(pokemonId: int):
    newSet = [pokemon for pokemon in pokemonDataBase if pokemon["id"] != pokemonId]
    return {"data": newSet}