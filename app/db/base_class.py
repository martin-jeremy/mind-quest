from sqlalchemy.orm import DeclarativeBase

# Base for Alembic -> it need it to generate all migrations
class Base(DeclarativeBase):
    pass
