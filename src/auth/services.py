from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status

from src import settings


def create_access_token(data: dict) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = data.copy()
    to_encode.update({'exp': expire})

    return jwt.encode(
        payload=to_encode,
        key=settings.SECRET_KEY,
        algorithm=settings.ACCESS_TOKEN_ALGORITHM
    )


def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(
            jwt=token,
            key=settings.SECRET_KEY,
            algorithms=[settings.ACCESS_TOKEN_ALGORITHM]
        )
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except jwt.InvalidSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except jwt.InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
