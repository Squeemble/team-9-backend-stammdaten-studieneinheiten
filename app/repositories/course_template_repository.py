import uuid
from sqlalchemy.orm import Session
from app.models.course_template import CourseTemplate
from app.schemas.course_template import CourseTemplateCreate


def get_all(db: Session):
  return db.query(CourseTemplate).all()


def get_by_id(db: Session, template_id: str):
  try:
    template_uuid = uuid.UUID(template_id)
  except ValueError:
    return None
  return (
    db.query(CourseTemplate).filter(CourseTemplate.id == template_uuid).first()
  )


def create(db: Session, template: CourseTemplateCreate):
  db_template = CourseTemplate(**template.model_dump())
  db.add(db_template)
  db.commit()
  db.refresh(db_template)
  return db_template
