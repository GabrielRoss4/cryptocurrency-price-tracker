import config as cfg
from src.database_interface import DatabaseAPI
from src.crypto_interface.crypto_api import CryptoAPI
import src.initialize # This will run the initialization script


def main():
    for coin in cfg.COINS_OF_INTEREST:
        datapoint = CryptoAPI().get_coin_data(coin)
        DatabaseAPI().store_data(datapoint)

if __name__ == '__main__':
    main()