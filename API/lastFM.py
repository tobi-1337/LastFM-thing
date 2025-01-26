from baseAPI import baseAPI
from config import lastFM_key, lastFM_secret
import hashlib
import requests

class lastFMAPI(baseAPI):
    def __init__(self, api_key, api_secret):
        super().__init__('http://ws.audioscrobbler.com/2.0/')
        self.api_key = api_key
        self.api_secret = api_secret
    def get_auth_url(self, callback_url):
        return f"https://www.last.fm/api/auth/?api_key={self.api_key}&cb={callback_url}"
    
    def create_session(self, token):
        params = {
            'method' : 'auth.getSession',
            'api_key' : self.api_key,
            'token' : token
        }

        params['api_sig'] = self._generate_sinature(params)
        params['format'] = "json"

        return self._request("GET", "", params=params)
    
    def _generate_signature(self, params):
        sorted_params = "".join(f"{key}{value}" for key, value in sorted(params.items()))
        string_to_sign = sorted_params + self.api_secret
        return hashlib.md5(string_to_sign.encode()).hexdigest()