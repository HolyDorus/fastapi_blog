from pydantic import BaseModel


class AccessToken(BaseModel):
    access_token: str
    token_type: str

    class Config():
        orm_mode = True
