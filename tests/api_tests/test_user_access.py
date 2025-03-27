import requests


def test_admin_access(base_url):
    admin_token = "admin_mock_token"
    url = f"{base_url}/admin/dashboard"
    header = {"Authorization": f"Bearer {admin_token}"}
    response = requests.get(url, headers=header)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"


def test_regular_user_access(base_url):
    user_token = "user_mock_token"
    url = f"{base_url}/admin/dashboard"
    headers = {"Authorization": f"Bearer {user_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 403, f"Expected 403 but got {response.status_code}"


def test_unauthorized_access(base_url):
    invalid_token = "invalid_mock_token"
    url = f"{base_url}/admin/dashboard"
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 401, f"Expected 401 but got {response.status_code}"
