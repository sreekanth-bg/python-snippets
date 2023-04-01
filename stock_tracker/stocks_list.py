# script to read CSV from list scripts in file and convert into a list (with eror handling)
# python3 stock_list.py
# get list from https://www.amfiindia.com/research-information/other-data/categorization-of-stocks
# https://www1.nseindia.com/products/content/equities/indices/nifty_LargeMidcap_250.htm


from pandas import *
from nsepy import get_history
from datetime import date
 
# reading CSV file
data = read_csv("~/Downloads/niftylargemidcap250list.csv")
 
# converting column data to list
scripts = data['Symbol'].tolist()
print('original count:',len(scripts),'\nnot able to retreive history from below scripts')

for script in scripts:
    try:
        data = get_history(symbol=script, start=date(2015,1,1), end=date(2015,1,31))
        close = data['Prev Close'].iloc[0]
    except IndexError:
        print(script)
        scripts.remove(script)

print('Hence use below:\n')
print(scripts)




