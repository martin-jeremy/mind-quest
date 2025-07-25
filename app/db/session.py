from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Build engine
engine = create_engine(str(settings.DATABASE_URL), echo=True, future=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)


# Dependance FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
