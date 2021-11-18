import requests
import os
from datetime import datetime

APP_ID = os.environ.get('APP_ID_NUTRIX')
API_KEY = os.environ.get('API_KEY_NUTRIX')
BEARER_TOKEN = os.environ.get('BEARER_TOKEN_SHEETY')

GENDER = 'female'
WEIGHT = 40
HEIGHT = 149
AGE = 22

nutrix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

exercise_description = input('Tell me which exercises you did: ')

headers_nutrix = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

query = {
    'query': exercise_description,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

exercise_response = requests.post(url=nutrix_endpoint, json=query, headers=headers_nutrix).json()

date = datetime.today().strftime('%d/%m/%Y')
time = datetime.today().strftime('%X')

headers_sheety = {
    'Authorization': BEARER_TOKEN
}

for exercise in exercise_response['exercises']:
    exercise_name = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    sheet_data = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise_name,
            'duration': duration,
            'calories': calories 
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheet_data, headers=headers_sheety)
    print(response.json())