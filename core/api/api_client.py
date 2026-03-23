class APIClient:

    def __init__(self, request_context, base_url, headers):
        self.request = request_context
        self.base_url = base_url
        self.headers = headers

    def get(self, path):
        return self.request.get(
            f"{self.base_url}{path}",
            headers=self.headers,
        )

    def post(self, path, data=None):
        return self.request.post(
            f"{self.base_url}{path}",
            data=data,
            headers=self.headers,
        )