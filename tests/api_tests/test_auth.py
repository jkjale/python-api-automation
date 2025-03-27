import requests


def test_protected_api(base_url):
    headers = {
        "Authorization": "Bearer your_access_token_here"
    }
    response = requests.get(f"{base_url}/user/me", headers=headers)
    assert response.status_code == 200
    assert "data" in response.json()
