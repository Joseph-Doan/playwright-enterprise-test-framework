from core.api.api_client import APIClient

class DevicesService:

    def __init__(self, client: APIClient):
        self.client = client

    def get_devices(self):
    #    return self.client["client"].get(
    #        f"{self.client['base_url']}/api/devices",
    #        headers=self.client["headers"]
    #    )
        return self.client.get("/api/devices")