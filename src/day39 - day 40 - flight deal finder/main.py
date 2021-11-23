#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from data_manager import DataManager

sheety_endpoint = os.environ.get('SHEETY_PRICES_ENDPOINT')

dataManager = DataManager()
sheet_data = dataManager.get_data(sheety_endpoint)

for data in sheet_data:
    if data['iataCode'] == '':
        url = f"{sheety_endpoint}/{data['id']}"
        data = {
            'price': {
                'iataCode': 'TESTING'
            }
        }

        response = requests.put(url=url, json=data)
        print(response.json())