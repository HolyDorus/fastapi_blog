from datetime import datetime

from pydantic import BaseModel, validator, EmailStr


class UserBase(BaseModel):
    class Config():
        orm_mode = True


class UserRegistrationIn(UserBase):
    username: str
    email: EmailStr
    password: str

    @validator('username')
    def username_validator(cls, v):
        if not v.isalnum():
            raise ValueError('must be alphanumeric')

        if len(v) > 100 or len(v) < 3:
            raise ValueError(
                'must be more than 3 but less than 100 characters'
            )

        return v

    @validator('password')
    def password_validator(cls, v):
        if len(v) < 5:
            raise ValueError('must contain at least 8 characters')

        number_of_capitals = sum(character.isupper() for character in v)

        if number_of_capitals < 1:
            raise ValueError('must contain at least 1 capital letters')

        return v


class UserRegistrationOut(UserBase):
    id: int
    username: str
    email: EmailStr
    register_at: datetime


class UserMeShow(UserBase):
    id: int
    username: str
    email: EmailStr
    register_at: datetime
    is_active: bool
    is_admin: bool
