# main module which calls stock_tracker.py for calculating and sorting all scripts in list for given days
# cannot be used for 1 day, set any one end date (eday)
# scripts and days (period) are hard coded in the list
# python3 multi.py

import sys
import os
import datetime as dt
import pandas as pd
from collections import defaultdict
import collections, functools, operator
from stock_tracker import getdata

# list
scripts = ["RELIANCE","HDFCBANK","HINDUNILVR","PIDILITIND","ASIANPAINT","HDFCLIFE","TCS","TITAN","LT","HCLTECH","INFY"]
days    = [365,180,90,60,30,7,0]

#dict = { scripts[i] : i for i in range(0, len(scripts) ) }   # create dict from list
dict = {}   # empty dictionary
list = []   # empty list

# create an Empty DataFrame object with pre defined column names
df = pd.DataFrame(columns = ['Script','Last','Change','%Change'])

if __name__ == "__main__":
    for day in days:
        print(day, "days")
        eday = dt.date.today()
        #eday = dt.date(2021, 7, 15)                                    # use this for back tracking
        mydays = dt.timedelta(days=int(day))
        sday = eday-mydays
        df.drop(df.index, inplace=True)                                 # drop contents of dataframe
        for script in scripts:
            data=getdata(script,sday,eday)
            df.loc[len(df)] = data                                      # append new row (data) to df
            tuple = (data[0],data[3])                                   # create tuple
            list.insert(0,tuple)                                        # Add tuple to front of list
        print(df.sort_values(by=['%Change'], ascending=False))
        print("------------------")
    for x in list:                                                         
        dict.setdefault(x[0],[]).append(x[1])                                # add multiple values to a specific key in a dictionary
    result = {key: sum(values) for key, values in dict.items()}              # calculate sum of values
    df2 = pd.DataFrame.from_dict(result, orient ='index',columns=['Rating']) # convert dictionary into dataframe
    print(df2.sort_values(by=['Rating'], ascending=False))


    
