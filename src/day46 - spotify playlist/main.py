import requests
from bs4 import BeautifulSoup

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
hot_100_page = response.text

soup = BeautifulSoup(hot_100_page, 'html.parser')

song_titles = soup.find_all(name='h3', class_='a-no-trucate', id="title-of-a-story")

song_list = [song.getText().replace('\n', '') for song in song_titles]

print(song_list)

for song in song_list:
    print(song)