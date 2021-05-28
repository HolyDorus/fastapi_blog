from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.user.services import get_user_by_username
from src.auth.services import decode_access_token
from src.database import get_db
from src import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.LOGN_URL)


def get_current_username(token: str = Depends(oauth2_scheme)):
    data_from_token = decode_access_token(token)

    if data_from_token['sub'] != settings.ACCESS_TOKEN_SUB:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )

    return data_from_token.get('username')


def get_current_user(
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username)
):
    user = get_user_by_username(username, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found'
        )

    return user


def get_current_active_user(user: str = Depends(get_current_user)):
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='For activated users only'
        )

    return user
