import pytest

@pytest.fixture(scope="session")
def base_url():
    return "http://127.0.0.1:8080"

@pytest.fixture
def test_user():
    return {
        "username": "admin",
        "password": "password"
    }