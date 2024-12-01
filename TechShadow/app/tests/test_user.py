import pytest
from app.queries.user_queries import get_user

# from tsdb import create_connection

#  route tests
def test_get_all_users(test_client):
    response = test_client.get("/users")
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 3
    for i in range(3):
        assert data[i]["username"] == f"username_{i+1}"



def test_get_user(test_client):
    response = test_client.get("/user/1")
    data = response.get_json()
    assert response.status_code == 200
    assert data["username"] == "username_1"
    assert data["first_name"] == "first_name_1"
    assert data["last_name"] == "last_name_1"
    assert data["is_mentor"] == True
    assert data["is_shadower"] == False
    assert data["field"] == "field_1"
    assert data["email"] == "email_1"


def test_post_user(test_client):
    new_user = {
        "username": "New_User",
        "password": "New_User",
        "first_name": "New_fn",
        "last_name": "New_ln",
        "is_mentor": True,
        "is_shadower": False,
        "field": "New_field",
        "email": "New_email"
    }
    response = test_client.post("/user", json=new_user)
    data = response.get_json()
    user_id = data["userID"]
    assert response.status_code == 201
    assert data["message"] == f"User {user_id} created"

    check = test_client.get(f"/user/{user_id}")
    check_data = check.get_json()
    assert check.status_code == 200
    assert check_data["username"] == "New_User"
    assert check_data["first_name"] == "New_fn"
    assert check_data["last_name"] == "New_ln"
    assert check_data["is_mentor"] == True
    assert check_data["is_shadower"] == False
    assert check_data["field"] == "New_field"
    assert check_data["email"] == "New_email"

def test_update_user(test_client):
    updated_user = {
        "username": "Updated_User",
        "password": "Updated_Password",
        "first_name": "Updated_fn",
        "last_name": "Updated_ln",
        "is_mentor": False,
        "is_shadower": True,
        "field": "Updated_field",
        "email": "Updated_email"
    }

    response = test_client.put("/user/1", json=updated_user)
    data = response.get_json()
    user_id = data["userID"]
    assert response.status_code == 200
    assert data["message"] == f"User {user_id} updated"
    check = test_client.get(f"/user/{user_id}")
    check_data = check.get_json()
    assert check.status_code == 200
    assert check_data["username"] == "Updated_User"
    assert check_data["first_name"] == "Updated_fn"
    assert check_data["last_name"] == "Updated_ln"
    assert check_data["is_mentor"] == False
    assert check_data["is_shadower"] == True
    assert check_data["field"] == "Updated_field"
    assert check_data["email"] == "Updated_email"


def test_delete_user(test_client):
    response = test_client.delete("/user/1")
    data = response.get_json()
    user_id = 1
    assert response.status_code == 200
    assert data["message"] == f"User {user_id} deleted"
    with pytest.raises(RuntimeError, match="User not found"):
        get_user(user_id)
