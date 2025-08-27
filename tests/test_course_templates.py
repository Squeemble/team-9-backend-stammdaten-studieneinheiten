import uuid


def test_create_course_template(client):
  response = client.post(
    "/courses/templates", json={"name": "Mathe", "elective": False}
  )
  assert response.status_code == 200
  data = response.json()
  assert data["name"] == "Mathe"
  assert data["elective"] is False
  assert "id" in data


def test_get_course_template(client):
  create_resp = client.post(
    "/courses/templates/", json={"name": "GDI", "elective": False}
  )
  assert create_resp.status_code == 200
  template_id = create_resp.json()["id"]

  get_resp = client.get(f"/courses/templates/{template_id}")
  assert get_resp.status_code == 200
  data = get_resp.json()
  assert data["id"] == template_id
  assert data["name"] == "GDI"
  assert data["elective"] is False


def test_get_nonexistent_course_template(client):
  random_id = str(uuid.uuid4())

  response = client.get(f"/courses/templates/{random_id}")
  assert response.status_code == 404
  assert response.json()["detail"] == "Course Template not found"
