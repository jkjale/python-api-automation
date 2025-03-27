import requests


def test_update_user(base_url):
    user_id = 2
    updated_data = {
        "name": "Jane Doe",
        "job": "Senior Software Engineer"
    }
    response = requests.put(f"{base_url}/users/{user_id}", json=updated_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == updated_data["name"]
    assert response_data["job"] == updated_data["job"]


def test_update_nonexistent_user(base_url, invalid_data):
    updated_data = {
        "name": "Nonexistent User",
        "job": "Ghost Developer"
    }
    response = requests.put(f"{base_url}/users/{invalid_data}", json=updated_data)
    assert response.status_code == 404
