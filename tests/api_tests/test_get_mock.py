import pytest
import requests
from unittest.mock import patch


# using patch() without pytest-mock
@pytest.mark.parametrize("user_iddd", [1, 2, 3, 4])
def test_get_user_by_id(base_url, user_iddd):
    mock_response = {
        "data": {
            "id": user_iddd,
            "first_name": "John",
            "last_name": "Doe",
            "email": f"user{user_iddd}@reqres.in"
        }
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        response = requests.get(f"{base_url}/users/{user_iddd}")
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["id"] == user_iddd
        assert data["data"]["email"] == f"user{user_iddd}@reqres.in"


# using mocker.patch with pytest-mock installed
def test_get_user(mocker, base_url):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "name": "John Doe"}
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1