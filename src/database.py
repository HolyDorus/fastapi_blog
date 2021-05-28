from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src import settings


engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

# SQLAlchemy Session class
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# SQLAlchemy Base class
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
