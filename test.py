import pyupbit
import time
import datetime
import random

f=open("key.txt")
lines=f.readlines()
access=lines[0].strip()
secret=lines[1].strip()
upbit = pyupbit.Upbit(access, secret)

entire_ticker=pyupbit.get_tickers()

while True:
    while upbit.get_balance("KRW")>=5000:
        ticker=random.choice(entire_ticker)
        if ticker[0]=='B'or ticker[0]=='U':
            continue
        print(ticker)
        upbit.buy_market_order(ticker, 5000)
        time.sleep(0.1)
        
    MY=upbit.get_balances()
    print(MY)
    for ticker in MY:
        name=ticker['currency']
        _avg=float(ticker['avg_buy_price'])
        if name=='KRW':
            continue
        name="KRW-"+name
        print(name,upbit.get_balance(name))
        if (pyupbit.get_current_price(name)>=1.005*_avg) or  (pyupbit.get_current_price(name)<=0.95*_avg) :
            upbit.sell_market_order(name,upbit.get_balance(name)) # 전량 매도     
        time.sleep(0.2)
        
    time.sleep(1)
