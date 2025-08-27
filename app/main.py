from fastapi import FastAPI
from app.api import api_router
from app.core.db import Base, engine

from app.models import course_template

Base.metadata.create_all(bind=engine)

app = FastAPI(title="team-9-backend-service")
app.include_router(api_router)
