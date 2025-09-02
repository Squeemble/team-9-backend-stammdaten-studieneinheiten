from app.models.course import Course
from app.schemas.course import CourseCreate
from app.repositories.base import CRUDBase

course_crud = CRUDBase[Course, CourseCreate](Course)
