import requests


def test_login_and_fetch_data(base_url):
    login_url = f"{base_url}/login"
    credentials = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(login_url, json=credentials)
    assert response.status_code == 200
    token = response.json().get("token")
    assert token is not None
    headers = {"Authorization": f"Bearer {token}"}
    user_response = requests.get(f"{base_url}/users/2", headers=headers)
    assert user_response.status_code == 200