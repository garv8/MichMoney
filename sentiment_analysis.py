from textblob import TextBlob
import requests
import pandas as pd
import numpy as np
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from yahooquery import Ticker
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from statistics import mean
import random


import pickle

# Specify the path to your .pkl file
file_path = 'motley-fool-data.pkl'
result_dict = {}
comp = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "BRK-B", "TSLA", "LLY", "V", "AVGO", "UNH", "NVO", "JPM", "WMT", "MA", "XOM", "JNJ", "HD", "PG", "MRK", "COST", "ABBV", "ORCL", "CVX", "ASML", "ADBE", "CRM", "BAC", "KO", "AMD", "PEP", "AZN", "ACN", "NFLX", "MCD", "TMO", "CSCO", "PDD", "INTC", "ABT", "LIN", "TMUS", "WFC", "CMCSA", "INTU", "DHR", "DIS", "AMGN", "NKE", "PFE", "VZ", "QCOM", "TXN", "NOW", "CAT", "MS", "IBM", "PM", "BX", "UNP", "GE", "SPGI", "UPS", "AXP", "BA", "HON", "COP", "UBER", "ISRG", "LOW", "AMAT", "NEE", "BKNG", "GS", "RTX", "PLD", "SCHW", "BLK", "SYK", "T", "MDT", "ELV", "LMT", "VRTX", "DE", "TJX", "GILD", "SBUX", "BMY", "PANW", "CVS", "LRCX", "REGN", "C", "MDLZ", "PGR", "ETN", "AMT", "ADP", "MMC", "ADI", "CB", "MU", "ZTS", "CI", "ABNB", "BSX", "FI", "MELI", "ANET", "SO", "ITW", "KLAC", "SHW", "SNPS", "HCA", "EQIX", "DUK", "MO", "WDAY", "KKR", "CDNS", "ICE", "WM", "ARM", "CME", "NOC", "SLB", "MCO", "CRWD", "CSX", "BDX", "GD", "EOG", "USB", "MAR", "CL", "PYPL", "TGT", "MCK", "SNOW", "SCCO", "FDX", "TEAM", "CMG", "LULU", "MNST", "PNC", "MMM", "AON", "CTAS", "PH", "MPC", "FCX", "APD", "EPD", "APH", "PSX", "MRVL", "ROP", "DELL", "ECL", "TDG", "HUM", "TT", "ORLY", "NXPI", "CHTR", "EMR", "SPG", "APO", "MSI", "DHI", "RSG", "PXD", "ADSK", "MET", "NSC", "PSA", "OXY", "AJG", "WELL", "TFC", "EL", "PCAR", "DXCM", "GM", "CCI", "COF", "CRH", "CARR", "AFL", "FTNT", "AIG", "SRE", "STZ", "F", "ET", "HLT", "KHC", "IDXX", "MCHP", "ROST", "CPRT", "EW", "PCG", "KDP", "TRV", "AZO", "COR", "LEN", "VLO", "MSCI", "NEM", "NU", "HES", "O", "PAYX", "CNC", "ODFL", "WMB", "AEP", "KVUE", "KMB", "MRNA", "SQ", "GWW", "DLR", "DASH", "TEL", "NUE", "OKE", "BK", "DDOG", "KMI", "D", "ALL", "JCI", "SPOT", "IQV", "HSY", "LHX", "AMP", "SYY", "A", "FERG", "AME", "DOW", "CTSH", "LVS", "URI", "PRU", "MPLX", "ADM", "EA", "CEG", "FIS", "IBKR", "ARES", "PLTR", "FAST", "COIN", "YUM", "EXC", "BIIB", "GIS", "OTIS", "IT", "ROK", "GEHC", "PPG", "GPN", "VRSK", "ZS", "CMI", "XEL", "CSGP", "TTD", "KR", "EXR", "VEEV", "NDAQ", "VICI", "DD", "CTVA", "ON", "RCL", "BKR", "GFS", "ED", "IR", "ANSS", "MLM", "LYB", "HAL", "CCEP", "PEG", "FICO", "EFX", "VMC", "HPQ", "CDW", "CPNG", "DLTR", "PWR", "DG", "ACGL", "HUBS", "MDB", "MPWR", "SNAP", "DVN", "DFS", "TTWO", "EIX", "DAL", "NET", "FANG", "XYL", "BF-B", "WBD", "KEYS", "RBLX", "WST", "GLW", "RMD", "CAH", "AVB", "WEC", "CBRE", "SBAC", "ZBH", "SPLK", "MTD", "AWK", "WTW", "PINS", "BNTX", "FTV", "MBLY", "HIG", "RKT", "WY", "ALNY", "TROW", "CHD", "TSCO", "SYM", "FITB", "BR", "APTV", "GRMN", "STT", "EQR", "ULTA", "RJF", "NVR", "CCL", "HWM", "PHM", "WAB", "MTB", "ILMN", "MOH", "TW", "DTE", "STE", "ARE", "SE", "FE", "EBAY", "ETR", "HPE", "ROL", "ALGN", "LYV", "ICLR", "EXPE", "ZM", "OWL", "INVH", "VRSN", "HEI", "TDY", "BRO", "WBA", "BLDR", "DOV", "PTC", "IFF", "UWMC", "BAX", "FLT", "FCNCA", "SIRI", "ES"
]

num_elements_from_start = int(len(comp) * 0.3)

# Shuffle the input list
random.shuffle(comp)

# Select elements from the beginning
top_elements_from_start = comp[:num_elements_from_start]

# Select elements from the rest of the list
rest_of_the_list = comp[num_elements_from_start:]
num_elements_from_rest = int(len(comp) * 0.2)
top_elements_from_rest = random.sample(rest_of_the_list, num_elements_from_rest)

# Combine the two subsets
companies = top_elements_from_start + top_elements_from_rest

print(TextBlob("We are going to lose more money, the end is near").sentiment.polarity)
# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Load the object from the file
    loaded_object = pickle.load(file)
    for index, row in loaded_object.iterrows():
        if row['ticker'] in companies and row['ticker'] not in result_dict and row['q'] == '2022-Q2':
            testimonial = TextBlob(row['transcript'])
            result_dict[row['ticker']] = [row['q'], row['transcript'], testimonial.sentiment.polarity]
            print(row['ticker'], result_dict[row['ticker']][2], result_dict[row['ticker']][0])

scores = []
sectors = []
industries = []
marketcap = []
final = []
for ticker in companies:
    if ticker in result_dict:
        final.append(ticker)
        scores.append(result_dict[ticker][2])
        data = {}
        url_base = "https://finviz.com/quote.ashx?t="+ticker
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
        soup = BeautifulSoup(requests.get(url_base, headers=headers).content, 'html.parser')
        l = []
        # parse all values in table into dict
        for i, row in enumerate(soup.select('.snapshot-td2')):
            if i%2 == 0:
                key = row.text
            else:   
                data[key]= row.text
        try:
            data['Sector'] = soup.select('.quote-links')[0].select('.tab-link')[0].text
            data['Industry'] = soup.select('.quote-links')[0].select('.tab-link')[1].text
            print(data['Sector'])
        except e:
            print(e)
        if data['Market Cap'][-1] == 'B':
            data['Market Cap'] = float(data['Market Cap'][:-1])*10e9
        elif data['Market Cap'][-1] == 'M':
            data['Market Cap'] = float(data['Market Cap'][:-1])*10e6
        else:
            pass
        sectors.append(data['Sector'])
        industries.append(data['Industry'])
        marketcap.append(data['Market Cap'])

    
# Combine the Information Above and the Corresponding Tickers into a DataFrame
d = {'Symbol': final, 'Sector': sectors, 'Industry': industries, 'Market Cap': marketcap, 'Sentiment Score': scores}
# create dataframe from 
df = pd.DataFrame(data=d)

fig = px.treemap(df, path=[px.Constant("Sentiment Heatmap"), 'Sector', 'Industry', 'Symbol'], values='Market Cap',
                  color='Sentiment Score', hover_data=[],
                  color_continuous_scale=['#FF0000', "#000000", '#00FF00'],
                  color_continuous_midpoint=0)

fig.update_traces(textposition="middle center")
fig.update_layout(margin = dict(t=30, l=10, r=10, b=10), font_size=20)

with open('live_sentiment.html', 'a') as f:
    f.truncate(0)
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))