import pytest

from ui_tests.pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)