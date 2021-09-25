import pandas as pd
import re

inFileName = input("Enter the file name with people's names: ")

inFile = open(inFileName, "r")

data = pd.DataFrame(columns=['name','email'])
for line in inFile:
    names = line.split(";")
    for name in names:
        data = data.append({
       'name': name.split('<')[0],
        'email':re.findall(r'<([^"]*)>', name)
        }, ignore_index=True)

print(data)
inFile.close()
