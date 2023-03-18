import os
from binance.client import Client
import pandas as pd
import datetime, time

client = Client("YOUR api_key", "YOUR api_secret")

def get_data(howLong, curr, interval = "1d"):
    candle = []

    intervals = {
      '15m': Client.KLINE_INTERVAL_15MINUTE,
      '1h':  Client.KLINE_INTERVAL_1HOUR,      
      '4h':  Client.KLINE_INTERVAL_4HOUR,
      '1d':  Client.KLINE_INTERVAL_1DAY
    }

    untilThisDate = datetime.datetime.now()
    sinceThisDate = untilThisDate - datetime.timedelta(days=howLong)

    try:
            
        candle = client.get_historical_klines(curr, intervals[interval], str(sinceThisDate), str(untilThisDate))

    except Exception as e:
        print(e)


    return candle

# print(get_data(2, "ETHUSDT"))
