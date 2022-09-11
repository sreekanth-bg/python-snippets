# Input days and stock name as parameters. Ex: python tracker.py 30 KEI

import sys
import os
import datetime as dt
import pandas as pd
import numpy as np
from nsepy import get_history, get_quote

def getdata(stock,sday,eday):
    data = pd.DataFrame(get_history(symbol=stock, start=sday, end=eday,))
    data = data.reset_index()
    #close = data.at[0, 'Prev Close']    # Access a single value using a label.
    close = data['Prev Close'].iloc[0]
    last  = data['Last'].iloc[-1]
    tchange = round(last-close,2)
    ptchange = round(((tchange/close)*100),2)
    return (stock,last,tchange,ptchange)






