from alpha_vantage.timeseries import TimeSeries
from flask import Flask
import requests
import json
import re
from .sentiment import sentiment_score
from .config import *


app = Flask(__name__)


# Primary root of the app (entry point)
@app.route("/")
def home_view():
    return "<h1>💰 🐦</h1>"


# This is the main path which will be called by the frontend.
# It will return the data in the format required by the frontend.
@app.route("/stock/<symbol>")
def stock_view(symbol):
    master_dictionary = {}
    company_name_ = company_name(symbol)
    master_dictionary['alpha_vantage_time_series'] = time_series_data(symbol)
    master_dictionary['company_overview'] = company_overview(symbol)
    master_dictionary['tweet_ids'] = recent_tweets(symbol, company_name_)
    return master_dictionary


# Gettting the time series data from Alpha Vantage API
def time_series_data(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY)
    data, meta_data = ts.get_daily(symbol=symbol)
    return data


# This function will return the company overview for the given symbol.
# This contains essential information required by the users to understand a company.
def company_overview(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    return r.json()


# Using the twitter api to get the recent tweets for the given symbol.
def recent_tweets(symbol, company):

    url = f"https://api.twitter.com/2/tweets/search/recent?max_results=25&query=({symbol} OR {poi} OR \"{company}\" OR \"{company} is\" OR \"{company} was\" OR \"{company} will\") lang:en -is:retweet -is:reply -is:quote -has:links&sort_order=relevancy"
    payload = {}
    headers = {
        'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    api_dict = {}
    len_tweets = len(res['data'])
    for i in range(len_tweets):
        tweet_id = f"{res['data'][i]['id']}"
        k = sentiment_score(res['data'][i]['text'])*10
        if k > 100:
            k = 99
        if k < -100:
            k = -99
        api_dict[tweet_id] = k
    # print(json.dumps(api_dict, indent=4))

    return api_dict


# Using the dumbstock API to get the company name for the given symbol
# and also the exchange in which the company is listed.
def company_name(index):
    try:
        index = index.upper()
        with open("src/ticker_data_new.json") as f:
            data = json.load(f)
        stock_name = data[index]['name']
        if len(stock_name.split()) >= 3:
            return stock_name
        stock_name = re.sub(r'[^a-zA-Z]', ' ', stock_name)
        stock_name = stock_name.strip()
        return stock_name.split(' ', 1)[0]
    except KeyError:
        return "Not Found"
