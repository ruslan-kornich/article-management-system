from pydantic import BaseModel, EmailStr, HttpUrl, constr
import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=50)


class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=50)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None


from pydantic import BaseModel, HttpUrl, EmailStr
from datetime import datetime


class ArticleBase(BaseModel):
    title: str
    link: HttpUrl
    summary: str
    published: datetime
    author: str

    class Config:
        arbitrary_types_allowed = True


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(ArticleBase):
    pass


class ArticleSchema(ArticleBase):
    id: int

    class Config:
        from_attributes = True
