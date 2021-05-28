from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.blogs import models, schemas


def get_all_blogs(db: Session) -> list[models.Blog]:
    return db.query(models.Blog).all()


def get_blog(id: int, db: Session) -> models.Blog:
    blog = db.query(models.Blog).get(id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id={id} not found"
        )

    return blog


def create_blog(data: schemas.BlogCreate, db: Session) -> models.Blog:
    new_blog = models.Blog(**data.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(id: int, data: schemas.BlogUpdate, db: Session) -> models.Blog:
    blog = db.query(models.Blog).get(id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id={id} not found"
        )

    blog_dict = jsonable_encoder(blog)
    data_dict = data.dict()

    for field in blog_dict:
        if field in data_dict:
            setattr(blog, field, data_dict[field])

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def delete_blog(id: int, db: Session) -> None:
    blog = db.query(models.Blog).get(id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id={id} not found"
        )

    db.delete(blog)
    db.commit()
