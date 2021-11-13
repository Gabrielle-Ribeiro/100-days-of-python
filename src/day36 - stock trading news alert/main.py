import requests
import smtplib
import os

STOCK = 'GOOG'
COMPANY_NAME = 'Alphabet Inc'
PERCENT = 5

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

MY_EMAIL = os.environ.get("TEMP_EMAIL")
MY_PASSWORD = os.environ.get("TEMP_PASSWORD")

stock_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

diff_percent = (abs(difference) / float(yesterday_closing_price)) * 100

if diff_percent > PERCENT:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles'][:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}\nSource:{article['url']}" for article in articles]

    if difference > 0:
        diff = f'+{abs(int(diff_percent))}%'
    else:
        diff = f'+{abs(int(diff_percent))}%'

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gabrielleribeiro2010@gmail.com",
            msg=f"Subject:Alphabet Inc News: {diff}\n\n{formatted_articles[0]}"
        )
