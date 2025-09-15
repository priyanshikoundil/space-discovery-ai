from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Database URL (from env variable if set, fallback to local postgres)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/space_discovery_ai")

# Engine and session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI endpoints
def get_db():
    """
    Yields a database session and ensures it is closed properly.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

