import pytest
from app.queries.message_queries import get_message


def test_get_messages(test_client):
    response = test_client.get("/messages")
    data = response.get_json()
    assert response.status_code == 200

    assert isinstance(data, list)
    assert len(data) > 0
    for message in data:
        assert "messageID" in message
        assert "name" in message
        assert "email" in message
        assert "message_content" in message


def test_get_message(test_client):
    response = test_client.get("/message/1") 
    data = response.get_json()
    assert response.status_code == 200

    assert data["messageID"] == 1
    assert "name" in data
    assert "email" in data
    assert "message_content" in data


def test_create_message(test_client):
    new_message = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "message_content": "This is a test message.",
    }

    response = test_client.post("/message", json=new_message)
    data = response.get_json()
    message_id = data["messageID"]
    assert response.status_code == 201

    assert data["message"] == f"Message {message_id} created"
    message = get_message(message_id)
    assert message["name"] == new_message["name"]
    assert message["email"] == new_message["email"]
    assert message["message_content"] == new_message["message_content"]


def test_update_message(test_client):
    updated_data = {
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "message_content": "This is an updated test message.",
    }

    response = test_client.put("/message/1", json=updated_data) 
    data = response.get_json()
    message_id = data["messageID"]
    assert response.status_code == 200

    assert data["message"] == f"Message {message_id} updated"
    updated_message = get_message(message_id)
    assert updated_message["name"] == updated_data["name"]
    assert updated_message["email"] == updated_data["email"]
    assert updated_message["message_content"] == updated_data["message_content"]


def test_delete_message(test_client):
    response = test_client.delete("/message/1") 
    data = response.get_json()
    message_id = 1
    assert response.status_code == 200

    assert data["message"] == f"Message {message_id} deleted"
    with pytest.raises(ValueError, match="message not found"):
        get_message(message_id)