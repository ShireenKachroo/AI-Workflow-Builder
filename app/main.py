from fastapi import FastAPI

from app.api.home import router as home_router
from app.config import settings

from app.database.database import Base, engine
from app.database import models

from app.api.workflows import router as workflow_router

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

Base.metadata.create_all(bind=engine)

app.include_router(home_router)
app.include_router(workflow_router)