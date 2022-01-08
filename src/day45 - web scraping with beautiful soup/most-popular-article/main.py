from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = soup.find_all(name="a", class_="titlelink")
scores = soup.find_all(name="span", class_="score")

article_titles = []
article_links = []
for title in titles:
    article_titles.append(title.getText())
    article_links.append(title.get("href"))

article_scores = [int(score.getText().split()[0]) for score in scores]

max_value = max(article_scores)
max_index = article_scores.index(max_value)

print("The most popular article\n")
print(article_titles[max_index])
print(article_links[max_index])
print(article_scores[max_index])
