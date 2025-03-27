import pytest


@pytest.fixture
def base_url():
    return "https://reqres.in/api"


@pytest.fixture
def api_key():
    return "your_api_key"


@pytest.fixture
def invalid_user_id():
    return 9999


@pytest.fixture
def new_user_data():
    return {"name": "John Doe", "job": "Software Engineer"}


@pytest.fixture
def invalid_data():
    return {"name": "", "job": ""}


@pytest.fixture
def valid_token():
    return "your_valid_token_here"

@pytest.fixture
def invalid_token():
    return "invalid_token_here"