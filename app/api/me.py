"""
Sample endpoint to show authenticated user information
"""

from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()


@router.get("/me")
def read_me(current_user: dict = Depends(get_current_user)):
  return {"msg": f"Hello {current_user['username']}"}
