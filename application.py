import config as cfg
from src.database_interface import DatabaseAPI
from src.crypto_interface.crypto_api import CryptoAPI
from src.crypto_interface.get_oauth_token import GetOAuthToken
import src.initialize # This will run the initialization script


def main():
    oauth_token = GetOAuthToken().get_token()
    for coin in cfg.COINS_OF_INTEREST:
        datapoint = CryptoAPI().get_coin_data(coin_query=coin, oauth_token=oauth_token)
        DatabaseAPI().store_data(datapoint)


if __name__ == '__main__':
    main()