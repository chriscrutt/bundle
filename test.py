#########################################################
# gives author aditional privacy when commiting- delete #
from apis import api_key, api_secret  #
#########################################################

# Allowing for type hints cause why not
from typing import Optional, List

# setting up api keys
pub: str = api_key
priv: str = api_secret


# importing binance client
from binance.client import Client

client = Client(api_key, api_secret)


# importing date for a readable server time
from datetime import datetime

time_res = client.get_server_time()

print(
    "server time:",
    datetime.utcfromtimestamp(time_res["serverTime"] /
                              1000).strftime('%Y-%m-%d %H:%M:%S'))


# seeing if server is running
status = client.get_system_status()

print("server status:", status["msg"])


# pulling (average) price of ticker
avg_price = client.get_avg_price(symbol='WBTCBTC')

print("average price WBTC/BTC:", avg_price["price"])


# getting daily candles from past 21 days
tickers = client.get_klines(symbol="WBTCBTC", interval="1d", limit="21")


# creating an array for all highs and lows of candles
high: List[float] = []
low: List[float] = []


# appends highs and lows of candles to respective arrays
for candle in tickers:
    high.append(float(candle[2]))
    low.append(float(candle[3]))


# finds average highs and lows
highAverage = round(sum(high) / len(tickers) * 100000) / 100000
lowAverage = round(sum(low) / len(tickers) * 100000) / 100000

print("21 day average high:", highAverage, "| 21 day average low:", lowAverage)


# get median of an array
def my_median(sample: List[float]) -> float:
    n = len(sample)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(sample)[index]
    # Sample with an even number of observations
    return sum(sorted(sample)[index - 1:index + 1]) / 2


# finds median highs and lows
highMedian = round(my_median(high) * 100000) / 100000
lowMedian = round(my_median(low) * 100000) / 100000

print("21 day median high:", highMedian, "| 21 day median low:", lowMedian)