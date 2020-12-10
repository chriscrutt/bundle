#########################################################
# gives author aditional privacy when commiting- delete #
# Allowing for type hints cause why not                 #
from apis import cmc_key                                #
#########################################################

# allows type hint "optional" incase of NoneType
from typing import Optional

# allows the pulling of data from apis
from requests import Session

# exceptions for debugging from pulling data from apis
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# allows reading json outputs
import json

# converts time into readable date
from date_format import convert_date

# setting the api key to the cmc api key for readibility
api_key = cmc_key

# header to be pushed to the api
headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": api_key}

#creating a new session and giving it the above header
session = Session()
session.headers.update(headers)

# returns all the given coin's stats (the comment below is fixing a linting error)
def get_coin_stats(coin: str) -> Optional[int]:  # pylint: disable=E1136  # pylint/issues/3139

    # url to the api
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # parameters to be pushed to the api
    params = {
        "start": "1",
        "limit": "200",
        "convert": "BTC",
        "aux": "cmc_rank,volume_7d,volume_30d"
    }

    # using a try-except for pulling api data
    try:

        # setting response to data received
        response = session.get(url, params=params)

        # making that data readable
        data = json.loads(response.text)

        # find that coin symbol and set it's info to coin_data
        for coin_test in data["data"]:
            if coin_test["symbol"] == coin:

                # finally prints the coin we were looking for
                return coin_test

    # if it fails to pull info from api, print why
    except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        return print(e)



coin_data = get_coin_stats("BTC")

print(
    "Name:", coin_data["name"], "\nRank:", coin_data["cmc_rank"],
    f"\nPrice in BTC:",
    coin_data["quote"]["BTC"]["price"], "\n24 hour volume:",
    coin_data["quote"]["BTC"]["volume_24h"], "\n7 day volume:",
    coin_data["quote"]["BTC"]["volume_7d"], "\n30 day volume:",
    coin_data["quote"]["BTC"]["volume_30d"], "\nMarket cap:",
    coin_data["quote"]["BTC"]["market_cap"], "\n\n" +
    convert_date(coin_data['quote']["BTC"]['last_updated']))
