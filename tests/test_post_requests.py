import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():
    post_data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=post_data)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_post_missing_fields():
    incomplete_data = {"userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=incomplete_data)
    assert response.status_code in [201, 400, 422]
    assert "id" in response.json()


def test_create_post_empty_data():
    response = requests.post(f"{BASE_URL}/posts", json={})
    assert response.status_code in [201, 400, 422]
    assert "id" in response.json()


def test_create_post_invalid_data_types():
    invalid_data = {"title": 123, "body": 456, "userId": "one"}
    response = requests.post(f"{BASE_URL}/posts", json=invalid_data)
    assert response.status_code in [201, 400, 422]
    assert "id" in response.json()


def test_create_post_extra_fields():
    extra_data = {"title": "foo", "body": "bar", "userId": 1, "extra_field": "not_expected"}
    response = requests.post(f"{BASE_URL}/posts", json=extra_data)
    assert response.status_code in [201, 400]
    assert "id" in response.json()
