def test_create_device_invalid_payload(api_request_context, base_url, auth_header):
    payload = {
        "name": "Broken Device"
        # missing "status"
    }

    response = api_request_context.post(
        f"{base_url}/api/devices",
        data=payload,
        headers=auth_header
    )

    assert response.status == 422


def test_get_nonexistent_device(api_request_context, base_url, auth_header):
    response = api_request_context.get(
        f"{base_url}/api/devices/999999",
        headers=auth_header
    )

    assert response.status == 404


def test_delete_nonexistent_device(api_request_context, base_url, auth_header):
    response = api_request_context.delete(
        f"{base_url}/api/devices/999999",
        headers=auth_header
    )

    assert response.status == 404

def test_get_devices_returns_list(devices_service):
    response = devices_service.get_devices()

    assert response.status == 200
    assert isinstance(response.json(), list)


def test_create_device(api_request_context, base_url, auth_header):
    payload = {
        "name": "New Device",
        "status": "offline"
    }

    response = api_request_context.post(
        f"{base_url}/api/devices",
        data=payload,
        headers=auth_header
    )

    assert response.status == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["status"] == payload["status"]


def test_get_device_by_id(api_request_context, base_url, auth_header, created_device):
    device_id = created_device["id"]

    response = api_request_context.get(
        f"{base_url}/api/devices/{device_id}",
        headers=auth_header
    )

    assert response.status == 200
    assert response.json()["id"] == device_id


def test_update_device(api_request_context, base_url, auth_header, created_device):
    device_id = created_device["id"]

    payload = {
        "name": "Updated Device",
        "status": "online"
    }

    response = api_request_context.put(
        f"{base_url}/api/devices/{device_id}",
        data=payload,
        headers=auth_header
    )

    assert response.status == 200
    assert response.json()["name"] == "Updated Device"


def test_delete_device(api_request_context, base_url, auth_header, created_device):
    device_id = created_device["id"]

    response = api_request_context.delete(
        f"{base_url}/api/devices/{device_id}",
        headers=auth_header
    )

    assert response.status == 204
