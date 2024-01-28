import json
import requests
import random

data = {}

with open("./michmoney/static/ticker_list.json", "r") as ticker_file:
    tickers = json.load(ticker_file)

    with open("./michmoney/static/util/worldgeo.json", "r") as json_file:
        for country in json.load(json_file)["objects"]["world"]["geometries"]:
            # url = f"https://financialmodelingprep.com/api/v3/quote/USD{swapped_tickers[country['id']]}?apikey=16b8d4bcbe3a416e463e5b0d16611847"
            data[country["id"]]["percent_change"] = round(random.uniform(-1, 1), 3)

with open("./michmoney/static/ticker_list.json", "w") as ticker_file:
    json.dump(data, ticker_file, indent=4)

print(data)
