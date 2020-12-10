# TODO

## API stuff that the bot can do
### Binance
- [x] server time
- [x] server status
- [x] price
- [x] volume (any time period)
- [x] pseudo market cap (ask and bid depth volume)

### CoinMarketCap
- [x] price
- [x] volume (up to 30 days)
- [x] Market capitalization

### CoinGecko
- [x] servers status
- [x] price
- [x] market cap
- [ ] volume (any time period)
    - [x] volume (24h)
- [ ] Daily, monthly (etc) price/market cap change?

## Questions to be answered
- [ ] how many coins should we use?
- [ ] What should a coin have to drop below in order to sell and switch to another?
- [ ] should we invest in stablecoins?

## Goals
### Look at 2-3 funds:
- [ ] Long term fund with biannual & yearly volume & Market Cap as focus
- [ ] Medium Term Fund with coins being pulled from both Long Term Fund and Short Term Fund. Semi Aggressive with long term stability as well.
- [ ] Short Term Fund/Aggressive Focus on Daily and monthly volume increase in Market Cap
- [ ] Amount of Shares/Tokens?
    - [ ] How many ETFs would we need to create - for example if we had a total of $1,000,000 (including liabilities I dont know doesn't matter for the example) in assets, if we had would we want to split it into 50,000 shares to make it ~$20 per etf (starting).
    - [ ] Look at overall supply to price


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