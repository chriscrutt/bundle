#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apis import cmc_key

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'20',
  'convert':'BTC',
  'aux':'volume_7d,volume_30d'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cmc_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print("name:", data["data"][0]["name"], "| price",
          data["data"][0]["quote"]["BTC"]["price"], "| 24 hour volume:",
          data["data"][0]["quote"]["BTC"]["volume_24h"], "| 7 day volume:",
          data["data"][0]["quote"]["BTC"]["volume_7d"], "| 30 day volume:",
          data["data"][0]["quote"]["BTC"]["volume_30d"], "| market cap:",
          data["data"][0]["quote"]["BTC"]["market_cap"])

    print("name:", data["data"][15]["name"], "| price",
          data["data"][15]["quote"]["BTC"]["price"], "| 24 hour volume:",
          data["data"][15]["quote"]["BTC"]["volume_24h"], "| 7 day volume:",
          data["data"][15]["quote"]["BTC"]["volume_7d"], "| 30 day volume:",
          data["data"][15]["quote"]["BTC"]["volume_30d"], "| market cap:",
          data["data"][15]["quote"]["BTC"]["market_cap"])
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
