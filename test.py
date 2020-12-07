#########################################################
# gives author aditional privacy when commiting- delete #
# Allowing for type hints cause why not
from typing import List

from apis import api_key, api_secret

#########################################################

# setting up api keys
pub: str = api_key
priv: str = api_secret

# importing binance client
from binance.client import Client  # @ignore

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

# creating an array for all highs and lows of candles, as well as volume
high: List[float] = []
low: List[float] = []
volume: List[float] = []

# appends highs and lows of candles to respective arrays, as well as volume
for candle in tickers:
    high.append(float(candle[2]))
    low.append(float(candle[3]))
    volume.append(float(candle[5]))

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

# 21 day volume
print("21 day volume in WBTC of WBTC/BTC:", sum(volume))

#########################################################

# getting daily BTC candles from past 12 months
btc_tickers = client.get_klines(symbol="BTCUSDT", interval="1M", limit="12")

# creating an array for all highs and lows of candles, as well as volume
btc_volume: List[float] = []

# appends volumes to array
for btc_candle in btc_tickers:
    btc_volume.append(float(btc_candle[5]))

# 12 month volume
print("\n12 month volume in BTC of BTC/USDT:", sum(btc_volume))

#########################################################

# getting total depth of all orders of given ticker (up to 5000)
depth = client.get_order_book(symbol="BTCUSDT", limit=5000)

# setting up lists for all bids and asks
bids: List[float] = []
asks: List[float] = []

# calculating bid order market cap
for bid in depth["bids"]:
    bids.append(float(bid[1]))

print("\ncurrent ask market cap of BTC/USDT:", str(sum(bids)))

# calculating ask order market cap
for ask in depth["asks"]:
    asks.append(float(ask[1]))

print("current bid market cap of BTC/USDT:", sum(asks))

# print("\ndepth:", depth)
