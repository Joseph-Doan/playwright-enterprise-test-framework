class DevicesPage:
    def __init__(self, page):
        self.page = page

    @property
    def heading(self):
        return self.page.get_by_role("heading", name="Devices")

    @property
    def device_items(self):
        return self.page.locator("li")

    def is_loaded(self):
        return "devices" in self.page.url

