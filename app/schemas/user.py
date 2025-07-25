from pydantic import BaseModel, EmailStr
from datetime import datetime

# Query
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# API response
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attribute = True # To convert from SQLAlchemy ORM