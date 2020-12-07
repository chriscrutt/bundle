#########################################################
# gives author aditional privacy when commiting- delete #
from apis import api_key, api_secret  #
#########################################################

from binance.client import Client

pub = api_key
priv = api_secret

client = Client(api_key, api_secret)

time_res = client.get_server_time()

print(time_res)