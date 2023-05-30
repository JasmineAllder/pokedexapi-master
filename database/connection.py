from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://pokemon_ns7l_user:C41hU49rxZBpfBkFO3oe53CtWWasUoSh@dpg-cgup5n02qv28lbe93ji0-a.frankfurt-postgres.render.com/pokemon_ns7l"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base =declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()