import requests

class baseAPI:
    def __init__(self, base_url, auth_token=None):
        self.base_url = base_url
        self.auth_token = auth_token

    def _get_headers(self):
        return {'Authorization': f"Bearer {self.auth_token}"} if self.auth_token else {}

    def _request(self, method, endpoint, params=None, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()
        response = requests.request(method, url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()