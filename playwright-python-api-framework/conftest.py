import pytest
from playwright.sync_api import APIRequestContext, sync_playwright

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8080"

@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="session")
def auth_header(api_request_context, base_url):
    """
    Logs in and returns the Authorization header for future requests.
    """
    response = api_request_context.post(
        f"{base_url}/api/login",
        data={
            "username": "admin",
            "password": "password"
        },
        headers={"Content-Type": "application/json"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
