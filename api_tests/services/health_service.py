from __future__ import annotations

from typing import Any

from core.api.api_client import APIClient


class HealthService:
    """
    Service layer for health endpoint validation.
    """

    HEALTH_PATH = "/health"

    def __init__(self, api_client: APIClient) -> None:
        self.api_client = api_client

    def get_health(self) -> Any:
        return self.api_client.get(self.HEALTH_PATH)