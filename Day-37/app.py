import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
pixela_token = os.getenv("PIXELA_TOKEN")
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
GRAPH_NAME = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",


}
# response = requests.post(url=pixela_enpoint, json=parameters)

# print(response.text)
params = {
    "id": "graph2",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}
headers = {
    "X-USER-TOKEN": token
}

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
# response = requests.post(url=graph_endpoint, json=params, headers=headers)
# print(response.text)


# post pixel
today = dt.datetime.now()
create_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "22"

}


post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_NAME}"
print(post_pixel_endpoint)
response = requests.post(
    url=post_pixel_endpoint, json=create_pixel_params, headers=headers)

print(response.text)
