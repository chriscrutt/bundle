#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apis import cmc_key
from temp_tests import convert_date

parameters = {
    "start": "1",
    "limit": "200",
    "convert": "BTC",
    "aux": "cmc_rank,volume_7d,volume_30d"
}

headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": cmc_key}

session = Session()
session.headers.update(headers)


def get_coin_stats(coin, params: dict):

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    try:
        response = session.get(url, params=params)
        data = json.loads(response.text)

        coin_data = {}

        for coin_test in data["data"]:
            if coin_test["symbol"] == coin:
                coin_data = coin_test

    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return print(e)

    return print(
        "Name:", coin_data["name"], "\nRank:", coin_data["cmc_rank"],
        f"\nPrice in {params['convert']}:",
        coin_data["quote"][params["convert"]]["price"], "\n24 hour volume:",
        coin_data["quote"][params["convert"]]["volume_24h"], "\n7 day volume:",
        coin_data["quote"][params["convert"]]["volume_7d"], "\n30 day volume:",
        coin_data["quote"][params["convert"]]["volume_30d"], "\nMarket cap:",
        coin_data["quote"][params["convert"]]["market_cap"], "\n\n" + convert_date(coin_data['quote'][params['convert']]['last_updated']))



get_coin_stats("BTC", parameters)

# try:
#     response = session.get(url, params=parameters)
#     data = json.loads(response.text)
#     print(

#     print("name:", data["data"][15]["name"], "| price",
#           data["data"][15]["quote"]["BTC"]["price"], "| 24 hour volume:",
#           data["data"][15]["quote"]["BTC"]["volume_24h"], "| 7 day volume:",
#           data["data"][15]["quote"]["BTC"]["volume_7d"], "| 30 day volume:",
#           data["data"][15]["quote"]["BTC"]["volume_30d"], "| market cap:",
#           data["data"][15]["quote"]["BTC"]["market_cap"])
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#     print(e)