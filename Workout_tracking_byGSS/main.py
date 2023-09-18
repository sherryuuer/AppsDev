import requests
import datetime
import os


API_ID = os.environ["nutritionix_apiid"]
API_KEY = os.environ["nutritionix_apikey"]
bearer_token = os.environ["sheety_bearer_token"]
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/f12e654105095c2388e43575f5eb5977/sallyWorkoutsTracking/workouts"

date_today = datetime.datetime.now().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H:%M:%S")

user_query = input("Tell me what did you do today:")
user_gender = "female"
user_weight = 49
user_height = 160.4
user_age = 33

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
nutritionix_params = {
    "query": user_query,
    "gender": user_gender,
    "weight_kg": user_weight,
    "height_cm": user_height,
    "age": user_age
    }
response = requests.post(url=nutritionix_endpoint, headers=headers, json=nutritionix_params)
datas = response.json()
print(datas)
for data in datas["exercises"]:
    exercise = data["name"].title()
    duration = data["duration_min"]
    calories = data["nf_calories"]
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    sheety_params = {
        "workout": {
            "date": date_today,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, headers=headers, json=sheety_params)
    print(sheet_response.text)
