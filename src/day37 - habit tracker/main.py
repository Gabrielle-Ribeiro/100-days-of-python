import requests
import os
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'gabrielle'
TOKEN = os.environ.get('PIXELA_TOKEN')
GRAPHID = 'graph1'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Create the user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPHID,
    'name': 'Reading Graph',
    'unit': 'Pages',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# Create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'

today = datetime.today()
today = today.strftime('%Y%m%d')

pixel_config = {
    'date': today,
    'quantity': '30',
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}'

new_pixel_data = {
    'quantity': '40',
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}'

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)