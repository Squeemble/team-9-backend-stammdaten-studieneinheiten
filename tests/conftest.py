import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.db import Base, get_db
from app.main import app
from app.models import course_template


# Test DB Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./tests/test.db"
engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False)


# Dependency override
def override_get_db():
  db = TestingSessionLocal()
  try:
    yield db
  finally:
    db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def clean_db():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)
  yield


@pytest.fixture
def client():
  return TestClient(app)
