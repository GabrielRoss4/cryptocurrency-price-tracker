import requests
import config as cfg
from traceback import print_exc

class GetCoinIDs(object):
    def __init__(self, api_key=cfg.API_KEY):
        self.url = "https://bravenewcoin.p.rapidapi.com/asset"
        self.querystring = dict()
        self.querystring["status"] = "ACTIVE"
        self.headers = {
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': "bravenewcoin.p.rapidapi.com"
            }

    def get_IDs(self, querystring={"status":"ACTIVE"}):
        return requests.request("GET", self.url, headers=self.headers, params=querystring).json()

    
    def get_by_symbol(self, symbol):

        cur_result = self.get_IDs(querystring={"status":"ACTIVE", "symbol":symbol})
        return cur_result["id"]


    def get_by_name(self, name):
        '''
        Input:
        * name: <str> Name of coin to search by

        Returns the id # of the coin name provided
        '''
        cur_result = self.get_IDs(querystring={"status":"ACTIVE", "name":name})
        return cur_result["id"]
