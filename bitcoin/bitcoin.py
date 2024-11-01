import requests
import json
import sys

a = sys.argv

if len(a) == 1:
    sys.exit('Missing command-line argument')
elif len(a) > 2:
    sys.exit()

try:
    n = float(a[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  
    o = response.json()
except:
   requests.RequestException

rate = o['bpi']['USD']['rate_float']
price = rate * n
formatted_price = f"{price:,.4f}"
print(f'${formatted_price}')
