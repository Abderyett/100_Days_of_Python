import requests
import os
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("NUTRITION_ID")
api_key = os.getenv("NUTRITION_IX_API_KEY")


endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    "query": input("Tell me which excercises you did: "),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 190,
    "age": 34

}

headers = {"x-app-id": app_id, "x-app-key": api_key}

response = requests.post(url=endpoint, json=params, headers=headers)

data = response.json()

print(type(data))
print(data)

# ran 5K and cycled for 40 minutes.
