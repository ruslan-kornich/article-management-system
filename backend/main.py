from fastapi import FastAPI
from backend.api.routes import router as api_router
from backend.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)
