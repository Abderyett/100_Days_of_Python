import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')


client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_='+15017122661',
        to='+15558675310'
    )

print(message.sid)

api_key = "619d37bdffe48dd4c39b272f2befe14b"
location = "London"
parameters = {
    "lat": "36.5322102",
    "lon": "2.9918496",
    "exclude": "current,minutely,daily,alerts",
    "lang": "fr",
    "appid": api_key,
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
# print(weather_data["hourly"][0]["weather"][0])
sliced_list = weather_data["hourly"][0:13]

will_rain = False
for hour_data in sliced_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True

if will_rain:
    print("Bring umbrella")
