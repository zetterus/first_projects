import requests
from bs4 import BeautifulSoup
import json

url = "https://rozetka.com.ua/439383788/p439383788/"

result = requests.get(url)  # получаем ответ от сервера

doc = BeautifulSoup(result.text, "html.parser")  # создаём бс4 объект, для парсинга хтмл страницы и присваиваем его переменной

tags = doc.find_all("script")  # ищем в этом объекте теги "script"

string = tags[4].string  # выбираем 5й по счёту и делаем из него строку

test = json.loads(string)  # десериализуем строку

print("notebook price:", test['offers']["price"])  # получаем значение вложенного словаря с помощью ключей
