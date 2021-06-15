from query_helper import CoinQuery
import os


DATABASE_PATH = "historic-crypto-prices.db"
API_KEY = os.environ.get("API_KEY")

COINS_OF_INTEREST = [
    CoinQuery(coin_name="Bitcoin", coin_symbol="BTC"),
    CoinQuery(coin_name="Ethereum", coin_symbol="ETH"),
    CoinQuery(coin_name="Stellar", coin_symbol="XLM"),
    CoinQuery(coin_name="Litecoin", coin_symbol="LTC"),
    CoinQuery(coin_name="Ripple", coin_symbol="XRP"),
    CoinQuery(coin_name="Polkadot", coin_symbol="DOT"),
    CoinQuery(coin_name="Dogecoin", coin_symbol="DOGE"),
    CoinQuery(coin_name="Bitcoin Cash", coin_symbol="BCH"),
    CoinQuery(coin_name="Cardano", coin_symbol="ADA"),
    CoinQuery(coin_name="Uniswap", coin_symbol="UNI"),
    CoinQuery(coin_name="Polygon", coin_symbol="MATIC")
]