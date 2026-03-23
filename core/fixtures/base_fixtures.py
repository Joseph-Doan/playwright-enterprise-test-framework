import pytest

from core.api.api_client import APIClient


@pytest.fixture
def api_client(api_request_context,base_url, auth_header):
    return APIClient(api_request_context, base_url, auth_header)