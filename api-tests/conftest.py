import pytest

@pytest.fixture(scope="session")
def api_request_context(playwright):
    request_context = playwright.request.new_context(
        base_url="http://localhost:8080",
    )
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


@pytest.fixture
def api_client(api_request_context, base_url, auth_header):
    return {
        "client": api_request_context,
        "base_url": base_url,
        "headers": auth_header
    }