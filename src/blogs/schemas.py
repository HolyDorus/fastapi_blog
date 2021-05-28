from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True


class BlogShow(BlogBase):
    id: int


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass
