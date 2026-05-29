from fastapi.testclient import TestClient

def test_export_to_excel(client: TestClient):
    # Создать тестовое резюме
    resume_response = client.post(
        "/api/v1/resumes/",
        json={
            "passport": "1234 567890",
            "secondname": "Test",
            "firstname": "User",
            "email": "test@test.com",
            "phone": "+79001234567",
            "city": "Moscow",
            "address": "Test Address",
            "gender": "Мужской",
            "birth_date": "1990-01-01",
            "education_level": "высшее",
            "marital_status": "Холост",
            "has_children": False,
            "military_service": True,
            "position": "Tester",
            "work_experiences": [],
            "educations": [],
            "courses": [],
            "languages": [],
            "computer_skills": []
        }
    )
    resume_id = resume_response.json()["id"]
    
    # Экспорт
    export_response = client.post(
        "/api/v1/export/",
        json={
            "resume_ids": [resume_id],
            "format": "excel",
            "include_photo": True
        }
    )
    assert export_response.status_code == 200
    data = export_response.json()
    assert data["format"] == "excel"
    assert "filename" in data
