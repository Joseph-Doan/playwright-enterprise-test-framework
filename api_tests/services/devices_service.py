from core.api.api_client import APIClient


class DevicesService:

    def __init__(self, client: APIClient):
        self.client = client

    def get_devices(self):
        return self.client.get("/api/devices")

    def get_device_by_id(self, device_id: int):
        return self.client.get(f"/api/devices/{device_id}")

    def create_device(self, payload):
        return self.client.post("/api/devices", data=payload)

    def update_device(self, device_id: int, payload):
        return self.client.put(f"/api/devices/{device_id}", data=payload)

    def delete_device(self, device_id: int):
        return self.client.delete(f"/api/devices/{device_id}")