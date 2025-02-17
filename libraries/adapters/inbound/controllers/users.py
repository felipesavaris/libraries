from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config_database
from libraries.domain.entities.dtos import UserIn, UserOut # ver depois como fica  (factory)
from libraries.domain.entities.models import table_registry, User as UserModel

# load_dotenv(dotenv_path='/Users/felipe.savaris/developer/libraries/.env')
#  engine = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.')
engine = create_engine('sqlite:///libraries/adapters/outbound/db/alembic/libraries.db')  # (config_database.DATABASE_URL)

table_registry.metadata.create_all(engine) # MUDAR PARA PASTA DB

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# dependency
def get_db():  # mudar para pasta db
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut, status_code=201)
def create(user: UserIn, db=Depends(get_db)):
    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user