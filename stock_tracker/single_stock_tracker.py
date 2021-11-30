# Input days and stock name as parameters. Ex: python3 single_stock_tracker.py 180 TCS

import sys
import os
import datetime as dt
import pandas as pd
import numpy as np
from nsepy import get_history, get_quote

# Clear system; auto detects windows and Linux (os module required)
#os.system('cls' if os.name == 'nt' else 'clear')

# Increase the Terminal size in Pandas (to overwrite autodetect values)
# pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)

PARAM1 = sys.argv[1]
PARAM2 = sys.argv[2]

eday = dt.date.today()
days = dt.timedelta(days=int(PARAM1))
sday = eday-days

data = pd.DataFrame(get_history(symbol=PARAM2, start=sday, end=eday))
#data = get_history(symbol=PARAM2, start=sday, end=eday)
data = data.reset_index()

chg = []
pchg = []
tchg = []
ptchg = []
nh7 = []

close = data.at[0, 'Prev Close']    # Access a single value using a label.
count = tsum = 0

for index, row in data.iterrows():
    count += 1
    chg.append(round(row['Last'] - row['Prev Close'], 2))
    pchg.append(
        round(((row['Last'] - row['Prev Close'])/row['Prev Close'])*100.0, 2))
    tchg.append(round(row['Last'] - close, 2))
    ptchg.append(round(((row['Last'] - close)/close)*100.0, 2))
    nh7.append(round(row['High'] - row['Low']))
    tsum += (row['Prev Close'])

MA = tsum/count

data['Change'] = chg   		# Append  column in dataframe
data['%Change'] = pchg      # Append  column in dataframe
data['T Change'] = tchg     # Append  column in dataframe
data['%T Change'] = ptchg   # Append  column in dataframe
data['NH7'] = nh7   		# Append  column in dataframe

del_columns = ['Symbol', 'Series', 'Turnover', '%Deliverble', 'Volume', 'Trades', 'Deliverable Volume']
# Delete selected columns in dataframe
data.drop(del_columns, inplace=True, axis=1)
print(data)
# tdata = get_quote(PARAM2)
# data = data.append({
#     'Date': dt.date.today().strftime('%Y-%m-%d'),
#     'Prev Close': data.at[(count-1), 'Close'],
#     'Open': tdata['open'],
#     'High': tdata['dayHigh'],
#     'Low': tdata['dayLow'],
#     'Last': tdata['lastPrice'],
#     'Change': tdata['change'],
#     '%Change': tdata['pChange']}, ignore_index=True)
#
# TMA = (tdata['lastPrice'] - MA)
#
# print("\n", data)
# print("-"*197)
# print("{0:<147} {1:<8.2f} {2:<8.2f} {3} {4:<8.2f}".format(
#     ' AVERAGE:', np.mean(chg), np.mean(pchg), 'MA:', TMA))
# print("-"*197)
#
# # print ("\nToday: dayOpen: {0}, dayHigh: {1}, DayLow: {2}".format(tData['open'], tData['dayHigh'], tData['dayLow']),end =" ,") #end="" will print the below line here only
# #print("LTP: {0}, Change: {1}, Change%: {2:.2f}".format(tData['lastPrice'], tData['change'], ((tData['change'] / data.loc[count-1]['Close']) * 100.0)),end =" ,")
# #print("52Low%: {0:.2f}, 52High%: {1:.2f}".format(((tData['lastPrice']-tData['low52']) / tData['high52'])*100.0, ((tData['high52']-tData['lastPrice']) / tData['high52']*100.0) ))
