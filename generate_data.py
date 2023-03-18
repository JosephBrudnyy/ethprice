from get_data import get_data
import pandas as pd

def generate_table(candle):
    df = pd.DataFrame(candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms').dt.strftime("%Y-%m-%d %H-%M-%S")
    df.set_index('dateTime', inplace=True)

    df = df.drop(['open', 'high', 'low', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)

    return df


df1 = generate_table( get_data(365 * 10, 'BTCUSDT', interval='1d') )
df2 = generate_table( get_data(365 * 10, 'ETHUSDT', interval= "1d") )

df1.to_csv(f"data_BTCUSDT.csv")
df2.to_csv(f"data_ETHUSDT.csv")
