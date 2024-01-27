from textblob import TextBlob
import requests
import pandas as pd
import numpy as np


# data = np.load('seeking2020.npy', allow_pickle = True)
# print(type(data))
# company_list = []

import pickle

# Specify the path to your .pkl file
file_path = 'motley-fool-data.pkl'
result_dict = {}
companies = {"AAPL",
"MSFT",
"GOOGL",
"AMZN",
"NVDA",
"META",
"BRK-B",
"TSLA",
"LLY",
"V",
"AVGO",
"UNH",
"NVO",
"JPM",
"WMT",
"MA",
"XOM",
"JNJ",
"HD",
"PG",
"MRK",
"COST",
"ABBV",
"ORCL",
"CVX",
"ASML",
"ADBE",
"CRM",
"BAC",
"KO",
"AMD",
"PEP",
"AZN",
"ACN",
"NFLX",
"MCD",
"TMO",
"CSCO",
"PDD",
"INTC",
"ABT",
"LIN",
"TMUS",
"WFC",
"CMCSA",
"INTU",
"DHR",
"DIS",
"AMGN",
"NKE",
"PFE",
}
# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Load the object from the file
    loaded_object = pickle.load(file)
    for index, row in loaded_object.iterrows():
        if(row['ticker'] in companies and row['ticker'] not in result_dict and row['q'] == '2021-Q3'):
            testimonial = TextBlob(row['transcript'])
            result_dict[row['ticker']] = [row['q'], row['transcript'], testimonial.sentiment.polarity]
            print(row['ticker'], result_dict[row['ticker']][2], result_dict[row['ticker']][0])