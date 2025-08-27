import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.core.db import Base


class CourseTemplate(Base):
  __tablename__ = "CourseTemplates"

  id = Column(
    UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
  )
  name = Column(String, nullable=False)
  elective = Column(Boolean, default=False)
