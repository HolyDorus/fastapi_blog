from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.blog import schemas, services


router = APIRouter(prefix='/blogs', tags=['Blogs'])


@router.get('/', response_model=list[schemas.BlogShow])
def show_all(db: Session = Depends(get_db)):
    return services.get_all_blogs(db)


@router.get('/{id}', response_model=schemas.BlogShow)
def show_one(id: int, db: Session = Depends(get_db)):
    return services.get_blog(id, db)


@router.post(
    '/',
    response_model=schemas.BlogShow,
    status_code=status.HTTP_201_CREATED
)
def create(data: schemas.BlogCreate, db: Session = Depends(get_db)):
    return services.create_blog(data, db)


@router.put('/{id}', response_model=schemas.BlogShow)
def update(id: int, data: schemas.BlogUpdate, db: Session = Depends(get_db)):
    return services.update_blog(id, data, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    services.delete_blog(id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
