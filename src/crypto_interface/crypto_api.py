from crypto_interface.get_coin_IDs import GetCoinIDs
from crypto_interface.query_asset_price import QueryAssetPrice, DataPoint
import config as cfg

# I don't like that I'm importing config in two files (this one and query_asset_price)

'''Queries the API for crypto of interest'''

class CryptoAPI(object):
    def __init__(self):
        pass

    def get_coin_data(self, coin_query)->DataPoint:
        coin_ID = GetCoinIDs().get_by_symbol(symbol=coin_query.symbol)
        coin_data = QueryAssetPrice().get_ticker(query_id=coin_ID)
        coin_data.symbol = coin_query.symbol
        return coin_data

