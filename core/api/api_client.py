from playwright.sync_api import APIRequestContext
from core.config import BASE_URL

class APIClient:

    def __init__(self, request: APIRequestContext):
        self.request = request

    def get_devices(self):
        return self.request.get(f"{BASE_URL}/devices")