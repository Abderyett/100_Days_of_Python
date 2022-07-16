import requests
import os
from dotenv import load_dotenv

load_dotenv()
pixela_token = os.getenv("PIXELA_TOKEN")
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")

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
create_pixel_params = {
    "date": "20220716",
    "quantity": "22"

}
post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph2"
print(post_pixel_endpoint)
response = requests.post(
    url=post_pixel_endpoint, json=create_pixel_params, headers=headers)

print(response.text)
