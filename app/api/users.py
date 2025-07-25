from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_pwd
from app.logging_config import logger

router = APIRouter()

@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # check if email is already known
    logger.info(f"Creating user {user_in.email}")
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        logger.warning(f"User {user_in.email} already exists")
        raise HTTPException(status_code=400, detail="Email already registered")

    # create new user
    hashed_pwd = hash_pwd(user_in.password)
    user = User(email=user_in.email, password=hashed_pwd)
    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info(f"Created user {user_in.email}")
    logger.debug(f"User {user_in.id} added in database")

    return user