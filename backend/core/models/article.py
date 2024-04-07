from sqlalchemy import Column, Integer, String, DateTime
from backend.database.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    link = Column(String, unique=True, index=True)
    summary = Column(String)
    published = Column(DateTime)
    author = Column(String)
