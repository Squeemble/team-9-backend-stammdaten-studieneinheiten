from sqlalchemy.orm import Session
from app.models.course_template import CourseTemplate
from app.schemas.course_template import CourseTemplateCreate
from app.repositories.base import CRUDBase

course_template_crud = CRUDBase[CourseTemplate, CourseTemplateCreate](
  CourseTemplate
)
