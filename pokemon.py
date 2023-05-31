from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.connection import Base

class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    classification = Column(String(150))
    type1 = Column(String(50))
    type2 = Column(String(50))
    generation = Column(Integer)
    height_m = Column(Float)
    weight_kg = Column(Float, nullable=True)
    attack = Column(Float, nullable=True)
    pokedex_no = Column(Integer)

    stats = relationship("PokemonStats", backref="pokemon", uselist=False)

class PokemonStats(Base):
    __tablename__ = "pokemon_stats"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    height_m =Column(Float, nullable=True)
    weight_kg =Column(Float, nullable=True)
    attack =Column(Float, nullable=True)