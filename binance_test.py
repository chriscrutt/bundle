#########################################################
# gives author aditional privacy when commiting- delete #
# Allowing for type hints cause why not                 #
from apis import api_key, api_secret                    #
#########################################################

# for type hints
from typing import List

# importing binance client
from binance.client import Client

# importing date for a readable server time
from datetime import datetime

# to format the date we get from the server
from date_format import convert_date

# setting up api keys
pub = api_key
priv = api_secret

# setting up client functions will access
client = Client(pub, priv)

# get's current server time from Binance's API
time_res = client.get_server_time()

# converts its UNIX time to a readable date
serv = datetime.utcfromtimestamp(time_res["serverTime"] /
                                 1000).strftime("%Y-%m-%d %H:%M:%S")

# prints it
print("server time:", convert_date(serv))

#########################################################

# seeing if Binance's (api) servers are running
status = client.get_system_status()

# prints result
print("server status:", status["msg"])

#########################################################

# pulling (average) price of a ticker
avg_price = client.get_avg_price(symbol="WBTCBTC")

# prints that average
print("average price WBTC/BTC:", avg_price["price"])

#########################################################

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

# prints the 21 day average of the highs and lows
print("21 day average high:", highAverage, "| 21 day average low:", lowAverage)

#########################################################


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

# prints the 21 day median of the highs and lows
print("21 day median high:", highMedian, "| 21 day median low:", lowMedian)

#########################################################

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

# prints 12 month volume
print("\n12 month volume in BTC of BTC/USDT:", sum(btc_volume))

#########################################################

# getting total depth of all orders of given ticker (up to 5000)
depth = client.get_order_book(symbol="BTCUSDT", limit=5000)

# setting up lists for all bids
bids: List[float] = []

# calculating bid order market cap
for bid in depth["bids"]:
    bids.append(float(bid[1]))

# prints total volume of currently open bid orders
print("\ncurrent ask market cap of BTC/USDT:", str(sum(bids)))

#########################################################

# setting up lists for all asks
asks: List[float] = []

# calculating ask order market cap
for ask in depth["asks"]:
    asks.append(float(ask[1]))

# prints total volume of currently open ask orders
print("current bid market cap of BTC/USDT:", sum(asks))