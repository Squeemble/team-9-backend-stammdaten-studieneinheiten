from sqlalchemy import Column, String, Boolean, Integer
from app.core.db import Base, BaseIdMixin


class CourseTemplate(Base, BaseIdMixin):
  __tablename__ = "CourseTemplates"

  name = Column(String, nullable=False)
  elective = Column(Boolean, default=False)
