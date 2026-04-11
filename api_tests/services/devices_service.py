from __future__ import annotations

from typing import Any

from core.api.api_client import APIClient


class DevicesService:
    """
    Service layer for device-related API operations.
    """

    DEVICES_PATH = "/api/devices"

    def __init__(self, api_client: APIClient) -> None:
        self.api_client = api_client

    def get_devices(self) -> Any:
        return self.api_client.get(self.DEVICES_PATH)

    def create_device(self, payload: dict[str, Any]) -> Any:
        return self.api_client.post(self.DEVICES_PATH, data=payload)

    def get_device_by_id(self, device_id: int | str) -> Any:
        return self.api_client.get(f"{self.DEVICES_PATH}/{device_id}")

    def update_device(self, device_id: int | str, payload: dict[str, Any]) -> Any:
        return self.api_client.put(f"{self.DEVICES_PATH}/{device_id}", data=payload)

    def delete_device(self, device_id: int | str) -> Any:
        return self.api_client.delete(f"{self.DEVICES_PATH}/{device_id}")