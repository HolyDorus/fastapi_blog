from typing import Optional

from fastapi import HTTPException, status, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from src.user.services import get_user_by_username
from src.user.models import User
from src.auth.services import decode_access_token
from src.database import get_db


def get_current_username(
    credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())
) -> Optional[str]:
    token = credentials.credentials
    data = decode_access_token(token)
    return data.get('username')


def get_current_user(
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username)
) -> User:
    user = get_user_by_username(username, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found'
        )

    return user


def get_current_active_user(user: User = Depends(get_current_user)) -> User:
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='For activated users only'
        )

    return user
