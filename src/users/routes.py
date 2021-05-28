from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.users import schemas, services, models
from src.auth.permissions import get_current_user, get_current_active_user


router = APIRouter(prefix='/users', tags=['Users'])


@router.post(
    '/register',
    response_model=schemas.UserRegistrationOut,
    status_code=status.HTTP_201_CREATED
)
def register(data: schemas.UserRegistrationIn, db: Session = Depends(get_db)):
    return services.register_user(data, db)


@router.get('/get-current-user', response_model=schemas.UserMeShow)
def get_user(user: models.User = Depends(get_current_user)):
    return user


@router.get('/get-current-active-user', response_model=schemas.UserMeShow)
def get_active_user(user: models.User = Depends(get_current_active_user)):
    return user
