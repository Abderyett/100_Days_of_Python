import requests
api_key = "619d37bdffe48dd4c39b272f2befe14b"
location = "London"
parameters = {
    "lat": "40.741895",
    "lon": "-73.989308",
    "exclude": "current,minutely,hourly,alerts",
    "appid": api_key,
}

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)

print(data.json())
