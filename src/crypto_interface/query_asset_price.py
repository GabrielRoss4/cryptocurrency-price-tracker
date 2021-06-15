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
    def get_ticker(self, coin_query):
        '''
        
        '''
        query_string = {"assetId":coin_query.ID, "percentChange":"true"}
        response = requests.request("GET", self.url, headers=self.headers, params=query_string).json()
        data = self.format_data(coin_query, raw_response=response)
        return data 

    def format_data(self, coin_query, raw_response):
        '''
        
        '''
        response_data = raw_response["content"][0]
        cur_price = round(response_data["price"], 2)
        percent_change_day = response_data["pricePercentChange"]["change24h"]
        query_date = str(date.today())
        query_time = str(datetime.now().time())
        new_data_point = DataPoint(
            coin_name=coin_query.name,
            coin_symbol=coin_query.symbol,
            cur_price=cur_price,
            percent_change_day=percent_change_day,
            date=query_date,
            time=query_time)

        return new_data_point


class DataPoint(object):
    def __init__(self, coin_name=None, coin_symbol=None, cur_price=None, percent_change_day=None, date=None, time=None):
        self.coin_name = coin_name
        self.coin_symbol = coin_symbol
        self.fullname = f"{self.coin_name}_{self.coin_symbol}"
        self.cur_price = cur_price
        self.percent_change_day = percent_change_day
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.coin_name} ({self.coin_symbol})\nPrice: {self.cur_price}\nChange on the day: {self.percent_change_day}%\n{self.date} {self.time}"




