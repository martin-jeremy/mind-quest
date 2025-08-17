from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_pwd
from app.logging_config import logger
from typing import List

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=201)
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
    logger.debug(f"User {user.id} added in database")

    return user


@router.get("/", response_model=List[UserResponse])
def list_users(
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=100),
        db: Session = Depends(get_db)
):
    logger.info(f"Listing users {skip}/{limit}")
    users = db.query(User).offset(skip).limit(limit).all()
    logger.info(f"Found {len(users)} users")

    return users