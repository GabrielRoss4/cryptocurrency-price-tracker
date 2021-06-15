import requests
import config as cfg
from src.crypto_interface.get_oauth_token import GetOAuthToken
from datetime import date, datetime


class QueryAssetPrice(object):
    def __init__(self, api_key=cfg.API_KEY, oauth_token=GetOAuthToken().get_token()):
        self.url = "https://bravenewcoin.p.rapidapi.com/market-cap"
        self.oauth_token = oauth_token
        self.headers = {
            'authorization': f"Bearer {self.oauth_token}",
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': "bravenewcoin.p.rapidapi.com"
            }
    def get_ticker(self, query_id):
        '''
        
        '''
        query_string = {"assetId":query_id}
        raw_response = requests.request("GET", self.url, headers=self.headers, params=query_string)
        data = self.format_data(raw_response)
        return data 

    def format_data(self, name, raw_response):
        '''
        
        '''
        response_data = raw_response["content"][0]
        cur_price = round(response_data["price"], 2)
        percent_change_day = response_data["priceChangePercent"]["change24h"]+"%"
        query_date = date.today()
        query_time = datetime.now().time()
        new_data_point = DataPoint(
            coin_name=name,
            cur_price=cur_price,
            percent_change_day=percent_change_day,
            date=query_date,
            time=query_time)

        return new_data_point

    def clean_results(self, raw_response):
        '''Probably unnecessary method'''
        response = dict()
        raw_response = raw_response["content"][0]
        response["price"] = round(raw_response["price"], 2)
        response["day_change"] = raw_response["priceChangePercent"]["change24h"]+"%"
        response["date"] = date.today()
        response["time"] = datetime.now().time()

class DataPoint(object):
    def __init__(self, coin_name=None, coin_symbol=None, cur_price=None, percent_change_day=None, date=None, time=None):
        self.coin_name = coin_name
        self.coin_symbol = coin_symbol
        self.fullname = f"{self.coin_name} ({self.symbol})"
        self.cur_price = cur_price
        self.percent_change_day = percent_change_day
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.coin_name} ({self.coin_symbol})\nPrice: {self.cur_price}Change on the day: {self.percent_change_day}%\n{self.date} {self.time}"

'''{"content":
[{"id":"8574072a-e614-4cc3-8b7d-1eb4fd4e7a43",
"assetId":"f1ff77b6-3ab4-4719-9ded-2fc7e71cff1f",
"timestamp":"2021-06-12T04:45:00.000Z","marketCapRank":1,"volumeRank":1,
"price":35276.47924181477,"volume":380008.46661038435,"totalSupply":18732787,
"freeFloatSupply":18729886,"marketCap":660724434680.5571,"totalMarketCap":660826771746.8375,
"marketCapPercentChange":{"change24h":-4.61,"change7d":-6.04,"change30d":-30.03},
"totalMarketCapPercentChange":{"change24h":-4.61,"change7d":-6.04,"change30d":-30.03},
"volumePercentChange":{"change24h":-11.38,"change7d":14.21,"change30d":-30.22},
"pricePercentChange":{"change24h":-4.61,"change7d":-6.07,"change30d":-30.12}}]}'''



