from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

# Create the SQLAlchemy Engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
)

# Create a Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for all ORM models
Base = declarative_base()


def get_db():
    """
    Database Dependency

    Creates a database session for every request
    and closes it automatically after the request ends.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()