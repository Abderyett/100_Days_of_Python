import requests
import os
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("NUTRITION_ID")
api_key = os.getenv("NUTRITION_IX_API_KEY")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    "query": "ran 2 miles"
}

headers = {"x-app-id": app_id, "x-app-key": api_key}

response = requests.post(url=endpoint, json=params, headers=headers)

print(response)
