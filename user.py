import json
import pandas as pd

pd.set_option("display.max_rows", 999)

f = open('elastic_users_eu.txt',"r")

#read json doc from file using json.load()
#convert json string doc into dictionary using json.loads()
data = json.load(f)
df = pd.DataFrame(columns=['name','email'])
for user in data:
    df = df.append({
    'name': data[user]['username'],
    'email': data[user]['email']
    }, ignore_index=True)

print(df)    
f.close()

# curl -k -XGET "https://localhost:9200" \
# --header 'Authorization: ApiKey S0thYTBIZ0JsTUhnNUlQNGIxTDg6MVhORG5hdXlScS0tTG8wYVBQaDlWQQ=='


# echo -n "KKaa0HgBlMHg5IP4b1L8:1XNDnauyRq--Lo0aPPh9VA" | base64