from pydantic import BaseModel, validator

class Pokemon(BaseModel):
    name: str
    classification : str
    type1: str
    type2: str
    generation: int
    height_m: float
    weight_kg: float
    attack: float
    pokedex_no: int

    class Config():
        orm_mode =True

    
class PokemonResponseModel(Pokemon):
    id: int

    class Config():
        orm_mode =True