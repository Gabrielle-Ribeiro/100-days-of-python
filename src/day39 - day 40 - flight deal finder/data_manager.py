import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_data(self, sheety_get_endpoint):
        data = requests.get(url=sheety_get_endpoint)
        return data.json()['prices']


# dataManager = DataManager()
# dataManager.get_data()