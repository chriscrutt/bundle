# allows type hint "optional" incase of NoneType
from typing import Optional

# allows the pulling of data from apis
from requests import Session

# exceptions for debugging from pulling data from apis
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# allows reading json outputs
import json

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


print("servers are:", ping()["gecko_says"])

#########################################################


# returns all the given coin's stats (the comment below is fixing a linting error)
def info() -> Optional[int]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = "https://api.coingecko.com/api/v3/coins/markets"
    # using a try-except for pulling api data

    # parameters to be pushed to the api
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": "3",
        "price_change_percentage": "1h,24h,7d,14d,30d,200d,1y"
    }

    try:
        # setting response to data received
        response = session.get(url, params=params)
        # making that data readable
        data = json.loads(response.text)
        return data
    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return e


def take_info(info):
    for coin in info:
        print("name:", coin["name"], "\ncurrent price (usd):",
              coin["current_price"], "\nmarket cap:", coin["market_cap"],
              "\ntotal volume (24h):", coin["total_volume"], "\n")


take_info(info())