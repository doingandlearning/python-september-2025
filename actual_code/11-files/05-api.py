import requests
import csv

"""
METHOD -> GET, POST, DELETE, PATCH, PUT
URL    -> https://  http://  ftp:// ssh://
HEADERS -> key:value 
PARAMS  -> ?q=bananas&

https://newsapi.org/v2/everything?q=animals&from=2025-07-28&sortBy=publishedAt&apiKey=
"""
API_KEY = "" 
query = input("What do you want headlines about?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-28&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

with open("articles.csv", "a") as file:
  writer = csv.writer(file)
  for article in data["articles"]:
    writer.writerow([article["source"]["name"], article["author"], article["title"]])