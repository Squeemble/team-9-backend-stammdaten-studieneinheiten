from typing import Generic, TypeVar
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.db import BaseIdMixin

ModelType = TypeVar("ModelType", bound=BaseIdMixin)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
  def __init__(self, model: type[ModelType]):
    self.model = model

  def get(self, db: Session, id: int) -> ModelType | None:
    return db.query(self.model).filter(self.model.id == id).first()

  def get_all(self, db: Session) -> list[ModelType]:
    return db.query(self.model).all()

  def create(self, db: Session, obj_in: CreateSchemaType):
    obj = self.model(**obj_in.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

  def delete(self, db: Session, id: int) -> None:
    obj = db.query(self.model).filter(self.model.id == id).first()
    if obj:
      db.delete(obj)
      db.commit()
