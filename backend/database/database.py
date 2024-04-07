import os

from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base


from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///backend/database/test.db"
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
