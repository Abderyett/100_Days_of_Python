import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
import datetime as dt


load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
now = dt.datetime.now()
current_time = now.strftime("%H:%M:%S")


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
while True:
    if current_time == "07:45:00":
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"Good morning! Weather info: Temperature for today in Algiers is {temp_min}°C - {temp_max}°C.",
                from_='++19784806789',
                to='+213770241855'
            )
