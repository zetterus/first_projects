import requests
from bs4 import BeautifulSoup
import json

url = "https://rozetka.com.ua/439383788/p439383788/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all("script")

string = tags[4].string

test = json.loads(string)

print("notebook price:", test['offers']["price"])


