# create and manage the database connection

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


# Base class for all database models
class Base(DeclarativeBase):
    pass


# Create the database engine ... establish connection to out DB
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
)


# Factory for creating database sessions
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()