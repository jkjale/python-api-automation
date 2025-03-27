import requests


def test_api_key_auth(base_url, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 200
    assert "data" in response.json()


def test_missing_api_key(base_url):
    response = requests.get(base_url)
    assert response.status_code == 401, f"Expected 401 but got {response.status_code}"
    assert "error" in response.json(), "No error message received"


def test_invalid_api_key(base_url):
    headers = {"Authorization": f"Bearer invalid_key"}
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 403, f"Expected 403 but got {response.status_code}"
    assert "error" in response.json(), "No error message received"


def test_invalid_jwt_token(base_url):
    headers = {"Authorization": f"Bearer invalid_jwt_token"}
    response = requests.get(f"{base_url}/users/2", headers=headers)
    assert response.status_code in (401,403), f"Expected 401 or 403 but got {response.status_code}"
    assert "error" in response.json(), "No error message received"