# similar to mlulti.py but gives only total change output for given days
# cannot be used for 1 day, set ny one end date (eday)
# python3 multi_stock_tracker.py 180 


import sys
import os
import datetime as dt
import pandas as pd
from stock_tracker import getdata

#scripts = ["NIFTY BANK","NIFTY ENERGY"]
scripts = ["RELIANCE","TCS","HCLTECH","HDFCLIFE","ACRYSIL","IRCTC","TATAMOTORS","HDFCBANK","TATAPOWER","NIFTYBEES","PIDILITIND","TITAN","ASIANPAINT","TATACHEM","LT","TATAELXSI"]
days    = [180,90,60,30,7]

PARAM1 = sys.argv[1]

eday = dt.date.today()                      # use this for calculating from today
# eday = dt.date(2021, 7, 15)               # use this for back tracking
days = dt.timedelta(days=int(PARAM1))
sday = eday-days

dict = {}

# create an Empty DataFrame object
df = pd.DataFrame(columns = ['Script','Last','Change','%Change'])

if __name__ == "__main__":
    for script in scripts:
        data=getdata(script,sday,eday)
        df.loc[len(df)] = data            # append new row (data) to df
        dict[script] = data[3]

    print(dict) 
    print(df.sort_values(by=['%Change'], ascending=False))
    