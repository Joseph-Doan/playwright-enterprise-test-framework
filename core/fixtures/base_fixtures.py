import pytest

@pytest.fixture
def api_client(api_request_context, auth_header):
    return api_request_context