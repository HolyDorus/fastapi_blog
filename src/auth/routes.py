from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.user.services import get_user_by_username
from src.database import get_db
from src.auth import schemas, services


router = APIRouter(prefix='/auth', tags=['Authorization'])


@router.post('/login', response_model=schemas.AccessToken)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_username(form_data.username, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with username={form_data.username} not found'
        )

    if not services.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid password'
        )

    token = services.create_access_token({'username': user.username})

    return schemas.AccessToken(access_token=token, token_type='bearer')
