import pyupbit
import time
import datetime

def cal_target(ticker,k):
    df = pyupbit.get_ohlcv(ticker,"day")
    yesterday=df.iloc[-2]
    today=df.iloc[-1]
    yesterday_range=yesterday['high']-yesterday['low']
    target= today['open']+yesterday_range*k
    return target

access="truPjute8McA5dL6lxPaLITpEqCkiedA69U3IpVP"
secret="xuyCLfU2zbhcAFO7wcHnxINZMr9SSnGxnrvmpxXC"
upbit = pyupbit.Upbit(access, secret)

target=cal_target("KRW-BTC",0.5)
op_mode=False
hold=False
ticker="KRW-BTC"
k=0.5

while True:
   now=datetime.datetime.now()
   price=pyupbit.get_current_price(ticker)
   
   if now.hour == 9 and now.minute == 0 and 20 <= now.second <= 30:
       target=cal_target(ticker,k)
       time.sleep(10)
       op_mode=True
       
       
   if op_mode is True and price is not None and price>=target and hold is False:
       krw_balance=upbit.get_balance("KRW")
       upbit.buy_market_order(ticker,krw_balance)
       hold=True
       
   if now.hour==8 and now.minute== 59 and (50<=now.second<=59):
       if op_mode is True and hold is True:
           btc_balance = upbit.get_balance(ticker)
           upbit.sell_market_order(ticker,btc_balance)
           hold=False
       op_mode=False
       time.sleep(10)
       
   print(f"현재시간: {now} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")    
   
   
   time.sleep(1)
   
       
       