from fastapi import HTTPException, status
from sqlalchemy.sql import exists
from sqlalchemy.orm import Session

from src.user.utils import get_password_hash
from src.user import models, schemas


def get_user_by_username(username: str, db: Session) -> models.User:
    return db.query(models.User).filter(
        models.User.username == username
    ).first()


def is_username_exists(username: str, db: Session) -> bool:
    return db.query(exists().where(models.User.username == username)).scalar()


def is_useremail_exists(email: str, db: Session) -> bool:
    return db.query(exists().where(models.User.email == email)).scalar()


def register_user(data: schemas.UserRegistrationIn, db: Session):
    if is_username_exists(data.username, db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'User with username={data.username} already exists'
        )

    if is_useremail_exists(data.email, db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'User with email={data.email} already exists'
        )

    return create_user(data, db)


def create_user(data: schemas.UserRegistrationIn, db: Session):
    hashed_password = get_password_hash(data.password)

    user = models.User(
        **data.dict(exclude={'password'}),
        password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
