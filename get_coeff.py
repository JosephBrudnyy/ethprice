import pandas as pd
from scipy import stats

def create_diff_table(df):
    df_out = pd.DataFrame(df, columns=['close'])
    df_shifted = pd.DataFrame(df, columns=['close']) #day - 1

    df_shifted['close'] = df['close'].shift()
    df_shifted[0] = df['close'].iloc[0]

    df_out['close'] = ((df['close'] / df_shifted['close']) - 1) * 100

    return df_out
    



def get_coeff():

    data_btc = pd.read_csv('data_BTCUSDT.csv')
    data_eth = pd.read_csv('data_ETHUSDT.csv')

    btc_diff = ( create_diff_table(data_btc) ).fillna(0)
    eth_diff = ( create_diff_table(data_eth) ).fillna(0)

    return stats.pearsonr(btc_diff['close'], eth_diff['close']).statistic
