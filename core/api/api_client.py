class APIClient:

    def __init__(self, request_context, base_url, headers=None):
        self.request = request_context
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}

    def _url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, headers=None):
        return self.request.get(
            self._url(path),
            headers={**self.headers, **(headers or {})},
        )

    def post(self, path, data=None, headers=None):
        return self.request.post(
            self._url(path),
            data=data,
            headers={**self.headers, **(headers or {})},
        )

    def put(self, path, data=None, headers=None):
        return self.request.put(
            self._url(path),
            data=data,
            headers={**self.headers, **(headers or {})},
        )

    def delete(self, path, headers=None):
        return self.request.delete(
            self._url(path),
            headers={**self.headers, **(headers or {})},
        )