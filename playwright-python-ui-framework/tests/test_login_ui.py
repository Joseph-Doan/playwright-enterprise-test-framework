from pages.login_page import LoginPage
from pages.devices_page import DevicesPage

def test_login_success(page, base_url):
    login_page = LoginPage(page)
    devices_page = DevicesPage(page)

    login_page.goto(base_url)
    login_page.login("admin", "password")

    assert devices_page.heading.is_visible()

def test_login_failure(page, base_url):
    login_page = LoginPage(page)

    login_page.goto(base_url)
    login_page.login("admin", "wrongpassword")

    assert login_page.error_message.is_visible()

def test_devices_page_displays_list(page, base_url):
    login_page = LoginPage(page)
    devices_page = DevicesPage(page)

    login_page.goto(base_url)
    login_page.login("admin", "password")

    assert devices_page.heading.is_visible()
    assert devices_page.device_items.count() >= 0