from services.devices_service import DevicesService


def test_get_devices(api_client):
    service = DevicesService(api_client)
    response = service.get_devices()

    assert response.status == 200