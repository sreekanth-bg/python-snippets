#list all Ips in the subnet

from netaddr import *
import pandas as pd

pd.set_option("display.max_rows", 999)

ips = open('ips.txt',"r")

df = pd.DataFrame(columns=['cidr','first','last'])
with open("ips.txt") as ips:
    for ip in ips:
        ip = IPNetwork(ip)
        df = df.append({
        'cidr': ip.cidr,
        'first': ip[0],
        'last': ip[-1]
        }, ignore_index=True)

print(df)    
ips.close()
