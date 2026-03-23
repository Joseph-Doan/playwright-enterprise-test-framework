import pytest

@pytest.fixture(scope="session")
def api_request_context(playwright, base_url):
    request_context = playwright.request.new_context(
        base_url = base_url,
    )
    yield request_context
    request_context.dispose()


