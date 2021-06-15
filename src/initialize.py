'''
Creates database and tables for each crypto specified in the config.
If the cryptos list has been altered new tables will be created as
needed. Cryptos removed from the config file will not be deleted automatically
and will need to be removed from the database manually.

The database will contain a master table tracking all cryptos in the database
as well as a table for each crypto with the headers as follows:
current_price_usd | percent_change_24h | query_date | query_time
'''

import sqlite3
import config as cfg


# Will connect to db if it exists and if it does not will create it
connection = sqlite3.connect("historic-crypto-prices.db")
cursor = connection.cursor()

# Create master table if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS Master (all_tracked_cryptos TEXT PRIMARY KEY, UNIQUE(all_tracked_cryptos))")
for crypto in cfg.COINS_OF_INTEREST:
    # Update with all cryptos in config not in master
    cursor.execute(f"INSERT OR IGNORE INTO Master(all_tracked_cryptos) VALUES(?)", (crypto.fullname,))
    connection.commit()
    # Create all tables from config that dont exist 
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {crypto.fullname}(current_price_usd, percent_change_24h, query_date, query_time, PRIMARY KEY(query_date, query_time))")
    connection.commit()

connection.close()