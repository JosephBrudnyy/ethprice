from get_coeff import get_coeff
from get_data import get_data
import datetime, time

import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def main():
    coeff = get_coeff()

    eth_prices = get_data(1, "ETHUSDT", interval='1h')
    btc_prices = get_data(1, "BTCUSDT", interval='1h')

    
    eth_price_now = float( eth_prices[-1][4] )  
    eth_price_before = float( eth_prices[-2][4] )

    btc_price_now = float( btc_prices[-1][4] )
    btc_price_before = float( btc_prices[-2][4] )

    ETH_growth_now = eth_price_now / (eth_price_now - (btc_price_now * (1 - coeff)) - 1) 
    ETH_growth_before = eth_price_before / (eth_price_before- (btc_price_before * (1 - coeff)) - 1) 



    alpha = ETH_growth_now / ETH_growth_before 


    nowTime = datetime.datetime.now()

    if alpha > 1.01:
        print("ETH рост на {alpha}%. Собственная цена: ", ETH_growth_now)
    else:
        print(F"{nowTime} ETH роста не наблюдается. Собственная цена: ", ETH_growth_now)




if __name__ == "__main__":
    set_interval(main, 10)