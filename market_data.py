from typing import Optional, List

# allows the pulling of data from apis
from requests import Session

# exceptions for debugging from pulling data from apis
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# allows reading json outputs
import json

# imports... time stuff
from time import sleep

from coin_ranking import main

# header to be pushed to the api
headers = {"Accepts": "application/json"}

#creating a new session and giving it the above header
session = Session()
session.headers.update(headers)

coin_sorter: List[dict] = []


# returns all the given coin's stats (the comment below is fixing a linting error)
def info(id) -> Optional[dict]:  # pylint: disable=E1136  # pylint/issues/3139
    # url to the api
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
    # parameters to be pushed to the api
    params = {"vs_currency": "usd", "days": "30"}
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


test = main()
sleep(60)
yew = []
start = info(test[0]["id"])["market_caps"]
og_cap = start[0][1]
percent = test[0]["percent_of_basket"]
for k in range(721):
    yew.append([start[k][0], start[k][1] * percent / og_cap])

for i in range(len(test) - 1):
    sleep(60)

    start = info(test[i + 1]["id"])["market_caps"]
    og_cap = start[0][1]
    percent = test[i + 1]["percent_of_basket"]
    for j in range(721):
        yew[j][1] += start[j][1] * percent / og_cap
    # print(temp)
# print(yew)

from datetime import datetime

for i in yew:
    i[0] = datetime.utcfromtimestamp(i[0] / 1000).strftime('%Y-%m-%d %H:%M:%S')

# print(yew)

yew = str(yew)

yew = yew.replace("['", "")
yew = yew.replace("', ", "\t")
yew = yew.replace("], ", "\n")

print(yew)
# rank = main()

# top_coins = {}

# for i in rank:
#     top_coins[i["id"]] = []

# for j in top_coins:
#     data = info(j))
