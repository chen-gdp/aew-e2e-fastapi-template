from fastapi.testclient import TestClient

from task_api.main import create_app


def client() -> TestClient:
    return TestClient(create_app())


def test_health() -> None:
    response = client().get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_task_lifecycle_and_completed_filter() -> None:
    api = client()
    first = api.post("/tasks", json={"title": "Review AEW spec"})
    second = api.post("/tasks", json={"title": "Merge implementation"})
    assert first.status_code == 201
    assert second.status_code == 201

    completed = api.patch(f'/tasks/{first.json()["id"]}', json={"completed": True})
    assert completed.status_code == 200
    assert completed.json()["completed"] is True

    response = api.get("/tasks", params={"completed": "true"})
    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["Review AEW spec"]


def test_missing_task_returns_404() -> None:
    response = client().patch("/tasks/999", json={"completed": True})
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_blank_title_is_rejected() -> None:
    response = client().post("/tasks", json={"title": ""})
    assert response.status_code == 422
