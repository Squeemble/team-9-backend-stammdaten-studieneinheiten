import uuid
from pydantic import BaseModel


class CourseTemplateBase(BaseModel):
  name: str
  elective: bool


class CourseTemplateCreate(CourseTemplateBase):
  pass


class CourseTemplateRead(CourseTemplateBase):
  id: uuid.UUID
