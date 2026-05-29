from fastapi.testclient import TestClient

def test_search_by_fio(client: TestClient):
    response = client.get("/api/v1/search/by-fio?fio=Иванов")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_by_position(client: TestClient):
    response = client.get("/api/v1/search/by-position?position=Программист")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
