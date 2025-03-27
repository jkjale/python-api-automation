import requests


def test_login(base_url):
    url = f"{base_url}/login"
    credentials = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url, json=credentials)
    assert response.status_code == 200
    tokens = response.json()
    access_token = tokens.get("token")
    assert access_token is not None and access_token != ""
    return access_token


def test_protected_with_access_token(base_url):
    access_token = test_login(base_url)
    url = f"{base_url}/users/2"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_refresh_token(base_url):
    access_token = test_login(base_url)
    new_access_token = f"new_{access_token}"
    assert new_access_token != access_token
    assert new_access_token.startswith("new_")
    return new_access_token


def test_protected_with_refreshed_token(base_url):
    new_access_token = test_refresh_token(base_url)
    url = f"{base_url}/users/2"
    headers = {
        "Authorization": f"Bearer {new_access_token}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
