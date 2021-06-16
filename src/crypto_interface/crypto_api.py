from src.crypto_interface.get_coin_IDs import GetCoinIDs
from src.crypto_interface.query_asset_price import QueryAssetPrice, DataPoint
from src.crypto_interface.get_oauth_token import GetOAuthToken


'''Queries the API for crypto of interest'''

class CryptoAPI(object):
    def __init__(self):
        pass

    def get_coin_data(self, coin_query, oauth_token=GetOAuthToken().get_token())->DataPoint:
        coin_query.ID = GetCoinIDs().get_by_symbol(symbol=coin_query.symbol)
        coin_data = QueryAssetPrice(oauth_token=oauth_token).get_ticker(coin_query=coin_query)
        return coin_data

