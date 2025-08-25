from fastapi import FastAPI

from app.api import api_router

app = FastAPI(title="team-9-backend-service")
app.include_router(api_router)
