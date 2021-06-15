import requests
import config as cfg


# Cache OAuth token for 24h

class GetOAuthToken(object):
    def __init__(self, api_key=cfg.API_KEY):
        self.url = "https://bravenewcoin.p.rapidapi.com/oauth/token"
        self.payload = '''{
\"audience\": \"https://api.bravenewcoin.com\",
\"client_id\": \"oCdQoZoI96ERE9HY3sQ7JmbACfBf55RY\",
\"grant_type\": \"client_credentials\"
}'''
        self.headers = {
            'content-type': "application/json",
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': "bravenewcoin.p.rapidapi.com"
            }
    def get_token(self):
        raw_response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
        return raw_response["access_token"]

