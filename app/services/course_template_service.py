from sqlalchemy.orm import Session
from app.repositories import course_template_repository
from app.schemas.course_template import CourseTemplateCreate


# In this case, this file only contains wrappers and could be optional.
# For more commplex models, there might be more business logic
# required. This business logic should go here.


def list_course_templates(db: Session):
  return course_template_repository.get_all(db)


def get_course_template(db: Session, course_id: str):
  return course_template_repository.get_by_id(db, course_id)


def create_course_template(db: Session, course: CourseTemplateCreate):
  return course_template_repository.create(db, course)
