from sqlalchemy.orm import DeclarativeBase
from app.models.user import User  # noqa


# Base for Alembic -> it need it to generate all migrations
class Base(DeclarativeBase):
    pass
