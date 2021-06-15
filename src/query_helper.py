class CoinQuery(object):
    def __init__(self, coin_name, coin_symbol):
        self.name = coin_name
        self.symbol = coin_symbol
        self.fullname = f"{self.name}_{self.symbol}"
        self.ID = None
