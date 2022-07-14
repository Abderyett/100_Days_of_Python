import requests
import os
from dotenv import load_dotenv

load_dotenv()
pixela_token = os.getenv("PIXELA_TOKEN")

pixela_enpoint = "https://pixe.la/v1/users"
parameters = {
    "token": "0005D1361555FCF73C77F610F9A6A1EA",
    "username": "abderyett",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",


}
response = requests.post(url=pixela_enpoint, json=parameters)

print(response.text)
