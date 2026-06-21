from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from main.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
# every class will inherit from this class
Base = declarative_base()


def get_db():
    """This function is responsible for returning the info from the database to the current user (latest info that he added)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
