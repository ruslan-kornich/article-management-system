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


class ArticleSchema(BaseModel):
    id: int
    title: str
    link: str
    summary: str
    published: str
    author: str
