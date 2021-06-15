import sqlite3
import config as cfg
from traceback import print_exc

# Should be storing price information in different tables for
# different cryptos

class DatabaseAPI(object):
    def __init__(self, database=cfg.DATABASE_PATH):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def store_data(self, datapoint):
        '''
        Input:
        * data_point: <data_point> struct containing important crypto api query data

        Logs data point in appropriate SQLite table
        '''
        
        base_sql_cmd = f'''INSERT INTO {datapoint.fullname}(current_price_usd, percent_change_24h, query_date, query_time)
        VALUES(?, ?, ?, ?)'''

        try:
            self.cursor.execute(base_sql_cmd, (datapoint.cur_price, datapoint.percent_change_day, datapoint.date, datapoint.time))
            self.connection.commit()
            return True
        except: 
            print("Failed to add entry to database")
            print_exc()
            return False
        finally:
            self.cursor.close()

    def retrieve_data(self, datapoint):
        '''
        Retrieve data point with specified parameters.

        Returns False if no matches for coin_name. 
        Returns closest data point in time if matches for 
        coin_name and no matches for date/time.
        '''

        base_sql_cmd = f'''SELECT * FROM {datapoint.fullname} WHERE query_date=? AND query_time=?'''

        try:
            self.cursor.execute(base_sql_cmd, (datapoint.date, datapoint.time))
            query_result = self.cursor.fetchone()
            print("Exact match found")
        except:
            print("Unable to fetch datapoint")
            print_exc()

        if not query_result:
            print("No exact match. Fetching nearest datapoint.")
            try:
                base_sql_cmd = f'''SELECT * FROM {datapoint.fullname} ORDER BY ABS(? - query_date), ABS(? - query_time) LIMIT 1'''
                self.cursor.execute(base_sql_cmd, (datapoint.date, datapoint.time))
                query_result = self.cursor.fetchone()
            except:
                print("Unable to fetch closest datapoint")
                print_exc()
        
        self.cursor.close()
        return query_result

    def delete_data_point(self, datapoint):
        '''
        Deletes data point with specified parameters. 
        
        Returns False if no exact matches for coin_name, date, and time.
        '''
        cur_point = self.retrieve_data(datapoint)
        if cur_point:
            if input(f"Deleting {str(cur_point)}. Confirm y/n\n") == "y":
                try:
                    base_sql_cmd = f"DELETE FROM {cur_point.fullname} WHERE current_price_usd=? AND percent_change_24h=? AND query_date=? AND query_time=?"
                    self.cursor.execute(base_sql_cmd, (cur_point.cur_price, cur_point.percent_change_day, cur_point.date, cur_point.time))
                    return True
                except:
                    print("Unable to delete datapoint")
                    print_exc()
                    return False
        else:
            print("No datapoint found")
            return False
        
        self.cursor.close()

