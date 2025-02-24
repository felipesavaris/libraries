from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from libraries.config import config_database

engine = create_engine(config_database.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        try:
            db.close()
        except Exception as err:
            print(f'Error closing session: {err}')
            pass
