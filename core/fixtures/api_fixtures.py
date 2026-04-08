import pytest
from core.api.api_client import APIClient
from api_tests.services.devices_service import DevicesService


@pytest.fixture(scope="session")
def api_request_context(playwright, base_url):
    context = playwright.request.new_context(base_url=base_url)
    yield context
    context.dispose()


@pytest.fixture(scope="session")
def auth_header(api_request_context, base_url):
    response = api_request_context.post(
        f"{base_url}/api/login",
        data={
            "username": "admin",
            "password": "password"
        },
        headers={"Content-Type": "application/json"},
    )

    assert response.status == 200, response.text()

    token = response.json().get("access_token")
    assert token, "No access token returned"

    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="session")
def api_client(api_request_context, base_url, auth_header):
    return APIClient(
        api_request_context,
        base_url,
        headers={
            **auth_header,
            "Content-Type": "application/json"
        }
    )


@pytest.fixture
def devices_service(api_client):
    return DevicesService(api_client)