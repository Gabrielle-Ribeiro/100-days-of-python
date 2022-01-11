import requests
from bs4 import BeautifulSoup

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
hot_100_page = response.text

soup = BeautifulSoup(hot_100_page, 'lxml')

song_titles = soup.find_all(name='h3', class_="c-title", id="title-of-a-story")
# print(song_titles.getText())

song_list = [song.getText() for song in song_titles]

for song in song_list:
    print(song)

