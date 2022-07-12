import requests
from dotenv import load_dotenv
import datetime as dt
from datetime import timedelta
import os
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()
alpha_vintage_api = os.getenv("API_KEY_ALPHAVANTAGE")
news_api = os.getenv("NEW_API_KEY")
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vintage_api

}
response = requests.get(
    "https://www.alphavantage.co/query?", params=parameters)

response.raise_for_status()


data = response.json()["Time Series (Daily)"]


now = dt.datetime.now().date()

# before_yesterday = str(now-timedelta(days=3))[0:10]
# yesterday = str(now-timedelta(days=2))[0:10]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

# * Get the day before yesterday closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = yesterday_data['4. close']


difference = abs(float(yesterday_closing_price) -
                 float(day_before_yesterday_closing_price))

diff_percent = (difference/float(yesterday_closing_price))*100

if diff_percent >= 5:
    print("Get News")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_params = {
    "q": COMPANY_NAME,
    "from": now,
    "sortBy": "popularity",
    "apiKey": news_api
}
res = requests.get(
    "https://newsapi.org/v2/everything?", params=news_params)
res.raise_for_status()

news_data = res.json()
print(now)
print(news_data)


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
