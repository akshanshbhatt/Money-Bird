from alpha_vantage.timeseries import TimeSeries
from flask import Flask
import requests
import json
import re
from .sentiment import sentiment_score

ALPHA_VANTAGE_API_KEY = 'QK435OE020SU1TTR'
COIN_API_KEY = '26CF8175-1B85-4319-9C16-D5AADD50932E'

TWITTER_API_KEY = 'QWq26qOLj7sonhlKs3ORZKa7U'
TWITTER_API_SECRET = '1E4V64EPkX6BXZX3ZXzvIdaCP7v4EuPWMyWOUFCTo3SW9EFzqL'
TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKKmbAEAAAAAfbIdTcldWHkq0DWgmytLt4r3pgk%3DyjaDeWtcUNgSZKY1mddJBwzJDC1WraRfE8LpZmZIEswwXwr5E0'
TWITTER_ACESS_TOKEN = '4641622393-P3b9aZIE9gPY6IFG5MICKJ964IW0umaSeG9KNIw'
TWITTER_ACESS_TOKEN_SECRET = 'NkHsIAb79F8melspjopiO5djYO3h8JqwwG7DoGx3jIZVJ'

TWITTER_CLIENT_ID = 'elE2TTg3WkRwOU5QYVZtM3JtTkU6MTpjaQ'
TWITTER_CLIENT_SECRET = 'qm05BcFtEaOkDz-FIQPBmJeiW7wGhRUqVp1RoiS0Naa0BWDoqW'


app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>💰 🐦</h1>"


@app.route("/stock/<symbol>")
def stock_view(symbol):
    master_dictionary = {}
    company_name_ = company_name(symbol)
    master_dictionary['alpha_vantage_time_series'] = time_series_data(symbol)
    master_dictionary['company_overview'] = company_overview(symbol)
    master_dictionary['tweet_ids'] = recent_tweets(symbol, company_name_)
    return master_dictionary


def time_series_data(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY)
    data, meta_data = ts.get_daily(symbol=symbol)
    return data


def company_overview(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    return r.json()


def recent_tweets(symbol, company):

    poi = person_of_interest(symbol)
    if poi == "":
        url = f"https://api.twitter.com/2/tweets/search/recent?max_results=25&query=({symbol} OR \"{company}\" OR \"{company} is\" OR \"{company} was\" OR \"{company} will\") lang:en -is:retweet -is:reply -is:quote -has:links&sort_order=relevancy"
    else:
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


def person_of_interest(symbol):
    poi = ""
    if symbol == 'AAPL':
        poi = '''"Tim Cook"'''
    elif symbol == 'GOOGL':
        poi = '''"Sundar Pichai'''
    elif symbol == 'MSFT':
        poi = '''"Satya Nadella"'''
    elif symbol == 'AMZN':
        poi = '''"Jeff Bezos" OR "Andy Jassy"'''
    elif symbol == 'FB':
        poi = '''"Mark Zuckerberg"'''
    elif symbol == 'TWTR':
        poi = '''"Jack Dorsey" OR "Parag Agarwal"'''
    elif symbol == 'CSCO':
        poi = '''"Larry Ellison"'''
    elif symbol == 'TSLA':
        poi = '''"Elon Musk"'''
    return poi


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
