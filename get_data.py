import os
from binance.client import Client
import pandas as pd
import datetime, time

client = Client("N1bdAy2zDhBWbfT9ieoO8vEEWoMxjP5gHGwZ1SVuUcUXIAh26kW1edB1FRYQPrA3", "ymu8l74h2druNeQPLN71HQdPpxBymx5vPeapy9CK1XeHi68pBT9YdsQD7WX6yKEF")

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
