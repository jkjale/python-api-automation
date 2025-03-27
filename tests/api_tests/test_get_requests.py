import pytest
import requests
from unittest.mock import patch


@pytest.mark.parametrize("user_iddd", [1, 2, 3, 4])
def test_get_user_by_id(base_url, user_iddd):
    response = requests.get(f"{base_url}/users/{user_iddd}")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == user_iddd


def test_get_users(base_url):
    response = requests.get(f"{base_url}/users?page=1")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0


def test_get_nonexistent_user(base_url, invalid_user_id):
    response = requests.get(f"{base_url}/users/{invalid_user_id}")
    assert response.status_code == 404


def test_get_users_pagination(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert data["page"] == 2
