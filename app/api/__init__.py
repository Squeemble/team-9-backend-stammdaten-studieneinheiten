from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from . import me, health

# Every route under this router requires the user to be authenticated
api_router = APIRouter(prefix="/api", dependencies=[Depends(get_current_user)])
api_router.include_router(me.router)
api_router.include_router(health.router)
