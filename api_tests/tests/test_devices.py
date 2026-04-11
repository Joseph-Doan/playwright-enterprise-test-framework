from __future__ import annotations


def test_get_devices(devices_service):
    """
    Validate that the devices endpoint returns a successful response
    and a JSON list payload.
    """
    response = devices_service.get_devices()

    assert response.status == 200, (
        f"Expected 200 from /api/devices, got {response.status}. "
        f"Body: {response.text()}"
    )

    payload = response.json()

    assert isinstance(payload, list), (
        f"Expected list response from /api/devices, got: {payload}"
    )


def test_create_device(devices_service):
    payload = {
        "name": "Test Device",
        "type": "sensor",
        "status": "active",
    }

    response = devices_service.create_device(payload)

    assert response.status == 201, (
        f"Expected 201 when creating device, got {response.status}. "
        f"Body: {response.text()}"
    )

    body = response.json()

    assert "id" in body, f"Expected created device to include id. Body: {body}"
    assert body["name"] == payload["name"]
    assert body["status"] == payload["status"]


def test_get_device_by_id(devices_service):
    create_payload = {
        "name": "Lookup Device",
        "type": "sensor",
        "status": "active",
    }

    create_response = devices_service.create_device(create_payload)
    assert create_response.status == 201, create_response.text()

    created = create_response.json()
    device_id = created["id"]

    response = devices_service.get_device_by_id(device_id)

    assert response.status == 200, (
        f"Expected 200 when fetching device by id, got {response.status}. "
        f"Body: {response.text()}"
    )

    body = response.json()
    assert body["id"] == device_id
    assert body["name"] == create_payload["name"]


def test_update_device(devices_service):
    create_payload = {
        "name": "Old Device",
        "type": "sensor",
        "status": "active",
    }

    create_response = devices_service.create_device(create_payload)
    assert create_response.status == 201, create_response.text()

    created = create_response.json()
    device_id = created["id"]

    update_payload = {
        "name": "Updated Device",
        "type": "sensor",
        "status": "inactive",
    }

    response = devices_service.update_device(device_id, update_payload)

    assert response.status == 200, (
        f"Expected 200 when updating device, got {response.status}. "
        f"Body: {response.text()}"
    )

    body = response.json()
    assert body["id"] == device_id
    assert body["name"] == update_payload["name"]
    assert body["status"] == update_payload["status"]


def test_delete_device(devices_service):
    create_payload = {
        "name": "Delete Device",
        "type": "sensor",
        "status": "active",
    }

    create_response = devices_service.create_device(create_payload)
    assert create_response.status == 201, create_response.text()

    created = create_response.json()
    device_id = created["id"]

    delete_response = devices_service.delete_device(device_id)

    assert delete_response.status in {200, 204}, (
        f"Expected 200 or 204 when deleting device, got {delete_response.status}. "
        f"Body: {delete_response.text()}"
    )


