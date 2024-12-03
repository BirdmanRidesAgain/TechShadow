import pytest
from app.queries.shadow_queries import get_shadow, get_shadows


def test_get_shadows(test_client):
    response = test_client.get("/shadows")
    assert response.status_code == 200, "Request failed"

    data = get_shadows()
    assert data is not None, "Response JSON is None"

    assert isinstance(data, list), "Response JSON is not a list"
    assert len(data) > 0, "No shadows returned"
    for shadow in data:
        assert "position" in shadow
        assert "job_description" in shadow
        assert "status" in shadow
        assert "location" in shadow


def test_get_shadow(test_client):
    shadow_id = test_client.get("/shadow/1")
    shadow = shadow_id.get_json()
    assert shadow_id.status_code == 200

    assert shadow["opportunityID"] == 1
    assert "position" in shadow
    assert "job_description" in shadow
    assert "is_remote" in shadow
    assert "location" in shadow


def test_create_shadow(test_client):
    new_shadow = {
        "position": "Software Developer Intern",
        "job_description": "Assist in developing web applications",
        "is_remote": True,
        "is_in_person": False,
        "status": "open",
        "required_skills": "Python, Django",
        "location": "Remote",
    }

    response = test_client.post("/shadow", json=new_shadow)
    data = response.get_json()
    shadow_id = data.get("shadowID")
    assert response.status_code == 201

    assert data["messsage"] == f"shadow {shadow_id} created"
    shadow = get_shadow(shadow_id)
    assert shadow["position"] == new_shadow["position"]
    assert shadow["job_description"] == new_shadow["job_description"]
    assert shadow["location"] == new_shadow["location"]


def test_update_shadow(test_client):
    updated_data = {
        "position": "Updated Position",
        "job_description": "Updated Job Description",
        "is_remote": False,
        "is_in_person": True,
        "status": "closed",
        "required_skills": "Updated Skills",
        "location": "Updated Location",
    }

    response = test_client.put("/shadow/1", json=updated_data)
    data = response.get_json()
    shadow_id = data.get("shadowID")
    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == f"shadow {shadow_id} updated"
    updated_shadow = get_shadow(shadow_id)
    assert updated_shadow["position"] == updated_data["position"]
    assert updated_shadow["job_description"] == updated_data["job_description"]
    assert updated_shadow["location"] == updated_data["location"]


def test_delete_shadow(test_client):
    response = test_client.delete("/shadow/1")
    data = response.get_json()
    shadow_id = 1
    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == f"shadow {shadow_id} deleted"
    with pytest.raises(RuntimeError, match="shadow not found"):
        get_shadow(shadow_id)
