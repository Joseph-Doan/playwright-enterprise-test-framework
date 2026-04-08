import pytest
import time


@pytest.fixture
def created_device(api_request_context, base_url, auth_header):
    """
    Creates a device before test and cleans it up after.
    """

    payload = {
        "name": f"test-device-{int(time.time())}",
        "status": "offline"
    }

    # CREATE
    response = api_request_context.post(
        f"{base_url}/api/devices",
        data=payload,
        headers=auth_header
    )

    assert response.status == 201, response.text()

    device = response.json()
    device_id = device["id"]

    yield device

    # CLEANUP
    api_request_context.delete(
        f"{base_url}/api/devices/{device_id}",
        headers=auth_header
    )