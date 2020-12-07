#########################################################
# gives author aditional privacy when commiting- delete #
from apis import api_key, api_secret  #
#########################################################

from binance.client import Client
from datetime import datetime

pub = api_key
priv = api_secret

client = Client(api_key, api_secret)

time_res = client.get_server_time()
status = client.get_system_status()

print(
    "server time:",
    datetime.utcfromtimestamp(time_res["serverTime"] /
                              1000).strftime('%Y-%m-%d %H:%M:%S'),
    "\nserver status:", status["msg"])


avg_price = client.get_avg_price(symbol='WBTCBTC')
print("average price WBTC/BTC:", avg_price["price"])

tickers = client.get_klines(symbol="WBTCBTC", interval="1d", limit="21")

high = []
low = []


def my_median(sample):
    n = len(sample)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(sample)[index]
    # Sample with an even number of observations
    return sum(sorted(sample)[index - 1:index + 1]) / 2


for candle in tickers:
    high.append(float(candle[2]))
    low.append(float(candle[3]))

highAverage = round(sum(high) / len(tickers) * 100000) / 100000
lowAverage = round(sum(low) / len(tickers) * 100000) / 100000

highMedian = round(my_median(high) * 100000) / 100000
lowMedian = round(my_median(low) * 100000) / 100000

print("21 day average high:", highAverage, "| 21 day average low:", lowAverage)
print("21 day median high:", highMedian, "| 21 day median low:", lowMedian)