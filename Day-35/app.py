import requests
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
    if hour_data["weather"][0]["id"] < 800:
        will_rain = True

if will_rain:
    print("Bring umbrella")
