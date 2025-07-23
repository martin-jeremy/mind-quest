from sqlalchemy import Column, String, Integer, DateTime, func
from app.db.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_connection_date = Column(DateTime(timezone=True), nullable=True)
