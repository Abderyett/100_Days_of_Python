import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
import datetime as dt
import time
from twilio.http.http_client import TwilioHttpClient


load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
now = dt.datetime.now()
current_hour = now.hour
current_min = now.minute


api_key = "619d37bdffe48dd4c39b272f2befe14b"
location = "London"
parameters = {
    "lat": "36.7753606",
    "lon": "3.0601882",
    "units": "metric",

    "lang": "fr",
    "appid": api_key,
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
temp_max = round(weather_data["daily"][0]["temp"]["max"])
temp_min = round(weather_data["daily"][0]["temp"]["min"])


# sliced_list = weather_data["hourly"][0:19]

# will_rain = False
# for hour_data in sliced_list:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 800:
#         will_rain = True
#         print()
is_time_match = True
while is_time_match:
    time.sleep(1)
    now = dt.datetime.now()
    current_hour = now.hour
    current_min = now.minute

    if current_hour == 7 and current_min == 42:
        proxy_client = TwilioHttpClient(
            proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

        client = Client(account_sid, auth_token, http_client=proxy_client)

        message = client.messages \
            .create(
                body=f"Good morning! Weather info: Temperature for today in Algiers is {temp_min}°C - {temp_max}°C.",
                from_='++19784806789',
                to='+213770241855'
            )
        is_time_match = False
