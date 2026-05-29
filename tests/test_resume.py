from fastapi.testclient import TestClient

def test_create_resume(client: TestClient):
    response = client.post(
        "/api/v1/resumes/",
        json={
            "passport": "1234 567890",
            "secondname": "Иванов",
            "firstname": "Иван",
            "patronymic": "Иванович",
            "email": "ivanov@example.com",
            "phone": "+79001234567",
            "city": "Москва",
            "address": "ул. Ленина, 1",
            "gender": "Мужской",
            "birth_date": "1990-01-01",
            "education_level": "высшее",
            "marital_status": "Холост",
            "has_children": False,
            "military_service": True,
            "position": "Программист",
            "work_experiences": [],
            "educations": [],
            "courses": [],
            "languages": [],
            "computer_skills": []
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["secondname"] == "Иванов"
    assert data["email"] == "ivanov@example.com"

def test_get_resumes(client: TestClient):
    response = client.get("/api/v1/resumes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
