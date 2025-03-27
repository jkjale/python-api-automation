import requests


def test_delete_user(base_url):
    user_id = 2
    response = requests.delete(f"{base_url}/users/{user_id}")
    assert response.status_code == 204
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code in (200, 404)


def test_delete_nonexistent_user(base_url, invalid_user_id):
    response = requests.delete(f"{base_url}/users/{invalid_user_id}")
    assert response.status_code == 404
