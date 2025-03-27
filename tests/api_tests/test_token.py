import requests


def test_refresh_token_success(base_url):
    login_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    login_repsonse = requests.post(f"{base_url}/login", json=login_data)
    assert login_repsonse.status_code == 200
    tokens = login_repsonse.json()
    refresh_token = tokens.get("refresh_token")
    refresh_data = {"refresh_token": refresh_token}
    refresh_repsonse = requests.post(f"{base_url}/refresh", json=refresh_data)
    assert refresh_repsonse.status_code == 200, "Token refresh failed"
    new_token = refresh_repsonse.json().get("access_token")
    assert new_token, "New access token was not received"


def test_refresh_token_failure(base_url):
    refresh_data = {
        "refresh_token": "invalid_refresh_token"
    }
    response = requests.post(f"{base_url}/refresh", json=refresh_data)
    assert response.status_code in (401, 403), f"Expected 401 or 403 but got {response.status_code}"
    assert "error" in response.json(), "No error message received"