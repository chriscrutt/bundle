# allows type hint "optional" incase of NoneType
from typing import Optional, List

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

coin_sorter: List[dict] = []


# returns all the given coin's stats (the comment below is fixing a linting error)
def info() -> Optional[dict]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = "https://api.coingecko.com/api/v3/coins/markets"
    # parameters to be pushed to the api
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": "40"
    }
    # using a try-except for pulling api data
    try:
        # setting response to data received
        response = session.get(url, params=params)
        # making that data readable
        data = json.loads(response.text)
        return data
    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return e


# print(info())


def use_info(info):
    for stuff in info:
        coin_sorter.append({
            "id": stuff["id"],
            "name": stuff["name"],
            "market_cap": stuff["market_cap"],
            "market_cap_rank": stuff["market_cap_rank"] - 1
        })


# print(coin_sorter)
use_info(info())
# print(coin_sorter, "\n")


def volume(range, id) -> Optional[dict]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart/range"

    minus = 86400 * range

    # parameters to be pushed to the api
    cur_time = time()
    params = {
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
        return data
    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return e


def conglom_vol(i, vol: List[dict]):

    while i < len(vol):
        yew = vol[i]["id"]

        my_vol = volume(365, yew)

        huge_vol = 0
        for big_num in my_vol["total_volumes"]:
            huge_vol += big_num[1]

        vol[i]["volume"] = huge_vol

        i += 1

    return vol


yew = conglom_vol(0, coin_sorter)


def vol_sort(e):
    return e['volume']


yew.sort(reverse=True, key=vol_sort)

for i in range(len(yew)):
    yew[i]["volume_rank"] = i

for i in range(len(yew)):
    yew[i]["rank"] = yew[i]["volume_rank"] + yew[i]["market_cap_rank"]


def all_sort(e):
    return e['volume_rank'] + e['market_cap_rank']


yew.sort(key=all_sort)

print("\n", yew)