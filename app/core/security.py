from fastapi import HTTPException, status


def get_current_user():
  """
  Returns a user object if the user is authenticated.
  Throws 401 UNAUTHORIZED otherwise
  """
  # TODO: Actually add authentication here
  return {"user_id": 1, "username": "admin", "role": "admin"}
  raise HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Not authenticated",
  )
