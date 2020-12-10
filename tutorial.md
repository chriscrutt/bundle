# Bundle - your friggin cryptos

## Introduction
We aim to create a robust, intuitive way to invest in a bundle of cryptocurrencies to help hedge against losses

## Technologies
We use fancy API technology oooh aaah and our functions are programmed by a 19 year-old student who knows half of what he's doing

## Mini Tut
### Prerequisites
1. get python 3 (git optional) - figure it out yourself
2. do `$ python --version` and if you see it's not python 3 then substitute `python` and `pip` with `python3` and `pip3` respectively
3. either download the zip or clone this repo onto your computer
4. do `$ pip install python-binance`

### binance_test.py
1. Delete the first 6 lines as they let the author/committers put API keys on a seperate file so y'all don't go hacking into our accounts
2. replace `api_key` and `api_secret` on lines 12 & 13 with your... api keys from Binance

**or (alternative)**
1. create a file called `apis.py`
2. in the `apis.py` file, create variables `api_key` and `api_secret` and set them to your respective Binance keys

### cmc_test.py
1. Delete the first 6 lines as they let the author/committers put API keys on a seperate file so y'all don't go hacking into our accounts
2. replace `cmc_key` on line 19 with your... api key from CoinMarketCap

**or (alternative)**
1. create a file called `apis.py` (if not already created)
2. in the `apis.py` file, create the variable `cmc_key` and set it to your CoinMarketCap api key

## gecko_test.py
1. They're friggen sick you don't even need an api everything is freeeeee

## Running
Do `$ python /Path/to/bundle/binance_test.py` and/or `$ python /Path/to/bundle/cmc_test.py` to run the programs yay