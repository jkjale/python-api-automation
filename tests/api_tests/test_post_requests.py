import pytest
import requests


@pytest.mark.parametrize(
    "namee, jobb",
    [
        ("John Doe", "Software Engineer"),
        ("Jane Smith", "Product Manager"),
        ("Alice Brown", "Designer")
    ]
)
def test_create_user_with_various_data(base_url, namee, jobb):
    user_data = {"name": namee, "job": jobb}
    response = requests.post(f"{base_url}/users", json=user_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["name"] == namee
    assert response_data["job"] == jobb


@pytest.mark.parametrize(
    "page, user_id",
    [(1, 2), (2, 4), (3, 6)]
)
def test_get_user_by_page(base_url, page, user_id):
    response = requests.get(f"{base_url}/users/{user_id}?page={page}")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == user_id


def test_create_user(base_url, new_user_data):
    response = requests.post(f"{base_url}/users", json=new_user_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["name"] == new_user_data["name"]
    assert response_data["job"] == new_user_data["job"]


def test_create_user_invalid_data(base_url, invalid_data):
    response = requests.post(f"{base_url}/users", json=invalid_data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data
