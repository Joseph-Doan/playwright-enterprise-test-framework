import pytest

@pytest.fixture(scope="session")
def base_url(config):
    return config.base_url

@pytest.fixture
def test_user():
    return {
        "username": "admin",
        "password": "password"
    }