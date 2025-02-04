import hashlib
import requests
import json

class lastFMAPI():
    def __init__(self, api_key, api_secret):
        self.base_url = 'http://ws.audioscrobbler.com/2.0/'
        self.api_key = api_key
        self.api_secret = api_secret

    def _request(self, method, endpoint="", params=None, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, params=params, json=data)
        response.raise_for_status()
        return response.json()
    
    def get_auth_url(self, callback_url):
        return f"https://www.last.fm/api/auth/?api_key={self.api_key}&cb={callback_url}"
    
    def create_session(self, token):
        params = {
            'method' : 'auth.getSession',
            'api_key' : self.api_key,
            'token' : token
        }

        params['api_sig'] = self._generate_signature(params)
        params['format'] = "json"
        return self._request("GET", "", params=params)
    
    def _generate_signature(self, params):
        sorted_params = "".join(f"{key}{value}" for key, value in sorted(params.items()))
        string_to_sign = sorted_params + self.api_secret
        return hashlib.md5(string_to_sign.encode()).hexdigest()

    def get_user_info(self, user):
        params = {
            'method' : 'user.getInfo',
            'user' : user,
            'api_key' : self.api_key,
            'format' : 'json'
        }
        print("Request params:", params)
        return self._request('GET', params=params)
    
    def get_top_artists(self, user, period='overall'):
        params = {
            'method' : 'user.getTopArtists',
            'user' : user,
            'period' : period,
            'api_key' : self.api_key,
            'limit' : 50,
            'format' : 'json'
        }
        return self._request('GET', params=params)
    
    def get_weekly_chart(self, user):
        params = {
            'method' : 'user.getWeeklyChartList',
            'user' : user,
            'api_key' : self.api_key,
            'format' : 'json'
        }
        #response = self._request('GET', params=params)
        #weekly_chart = response['chart']
        #print(weekly_chart)
        result = self._request('GET', params=params)
        return result['weeklychartlist']['chart']
    
    def get_weekly_artist(self, user, from_unix = None, to_unix = None):
        params = {
            'method' : 'user.getWeeklyArtistChart',
            'user' : user,
            'from' : from_unix,
            'to' : to_unix,
            'api_key' : self.api_key,
            'format' : 'json'
        }
        return self._request('GET', params=params)