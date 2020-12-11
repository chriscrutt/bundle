# allows type hint "optional" incase of NoneType
from typing import Optional

# allows the pulling of data from apis
from requests import Session

# exceptions for debugging from pulling data from apis
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# allows reading json outputs
import json

# imports... time stuff
from time import time

# header to be pushed to the api
headers = {"Accepts": "application/json"}

#creating a new session and giving it the above header
session = Session()
session.headers.update(headers)


# returns whether or not CoinGecko's server(s) are running (the comment below is fixing a linting error)
def ping() -> Optional[dict]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = "https://api.coingecko.com/api/v3/ping"
    # using a try-except for pulling api data
    try:
        # setting response to data received
        response = session.get(url)
        # making that data readable
        data = json.loads(response.text)
        return data
    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return e


# prints the answer to all your hopes and dreams
print("servers are:", ping()["gecko_says"], "\n")

#########################################################


# returns all the given coin's stats (the comment below is fixing a linting error)
def info() -> Optional[dict]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = "https://api.coingecko.com/api/v3/coins/markets"
    # parameters to be pushed to the api
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": "3",
        "price_change_percentage": "1h,24h,7d,14d,30d,200d,1y"
    }
    # using a try-except AGAIN for pulling api data
    try:
        # setting response to data received
        response = session.get(url, params=params)
        # making that data readable
        data = json.loads(response.text)
        return data
    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return e


# printing essential information for proof of concept
def take_info(info: dict) -> None:
    for coin in info:
        print("name:", coin["name"], "\ncurrent price (usd):",
              coin["current_price"], "\nmarket cap:", coin["market_cap"],
              "\ntotal volume (24h):", coin["total_volume"], "\n")


take_info(info())

#########################################################


def volume(range) -> Optional[dict]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"

    minus = 86400 * range

    # parameters to be pushed to the api
    cur_time = time()
    params = {
        "id": "bitcoin",
        "vs_currency": "usd",
        "from": str(cur_time - minus),
        "to": str(cur_time)
    }
    # using a try-except AGAIN for pulling api data
    try:
        # setting response to data received
        response = session.get(url, params=params)
        # making that data readable
        data = json.loads(response.text)
        return range, data
    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return e

def conglom_vol(vol_info: dict):
    range, vol = vol_info
    huge_vol = 0
    for big_num in vol["total_volumes"]:
        huge_vol += big_num[1]

    huge_vol = "{:,d}".format(round(huge_vol))
    print(f"over {range} days there has been a volume of ${huge_vol}")

conglom_vol(volume(365))