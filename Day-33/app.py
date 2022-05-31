from urllib import response
import requests
MY_LATITUDE = 43.643930
MY_LONGITUDE = -79.368970

# response = requests.get(url='http://api.open-notify.org/iss-now.json')

# # to Raise Error that could occur
# response.raise_for_status()
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# position = (latitude, longitude)

# print(position)

parameters = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE}

response = requests.get(
    url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise, sunset)
