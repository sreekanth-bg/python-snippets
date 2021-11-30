#get all events from statuspage and filter on maintenance

import requests
from getpass import getpass

# Replace with the correct URL
url = "https://api.statuspage.io/v1/pages/nwvc5p3sngnw/incidents"


#api_key = '21fb3926-9656-4e3b-acba-ab467a06eb07'
# Prompt the user for a password without echoing
api_key = getpass('api_key:')            


myResponse = requests.get(url,headers={'Authorization': api_key}, verify=False)
# For successful API call, response code will be 200 (OK)
jResponse = myResponse.json() if(myResponse.ok) else 0
for impact in jResponse:
        if impact['impact'] == 'maintenance': print(impact['resolved_at'], impact['name'],)  # impact=maintenance,none
