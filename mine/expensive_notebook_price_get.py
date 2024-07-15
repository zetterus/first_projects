import requests
from bs4 import BeautifulSoup

url = "https://rozetka.com.ua/439383788/p439383788/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all("script")

string = str(tags[4])
# print(string)
# print(string.find('"price":"'))
print(string[1255+9:1255+9+6])
