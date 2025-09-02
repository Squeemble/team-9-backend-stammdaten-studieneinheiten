from sqlalchemy.orm import Session
from app.repositories.course_repository import course_crud
from app.schemas.course import CourseCreate


# In this case, this file only contains wrappers and could be optional.
# For more commplex models, there might be more business logic
# required. This business logic should go here.


def list_course(db: Session):
  return course_crud.get_all(db)


def get_course(db: Session, template_id: int):
  return course_crud.get(db, template_id)


def create_course(db: Session, course: CourseCreate):
  return course_crud.create(db, course)
