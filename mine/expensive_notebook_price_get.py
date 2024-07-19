from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json

URL = "https://rozetka.com.ua/ua/search/?page=4&redirected=1&text="
PATH = "D:\\python\\first_projects\\not mine\\scraping\\Tech with Tim\\chromedriver.exe"
QUERY = input("TYPE YOUR REQUEST")

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get(URL + "+".join(QUERY.split(" ")))  # переходим по готовой ссылке с поисковым запросом

try:

    # находим количество страниц с результатами
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pagination__list")))
    pages = driver.find_element(By.CLASS_NAME, "pagination__list")
    max_pages = int(pages.text.split("\n")[-1])

    # записываем url и разбиваем его на куски для дальнейшей вставки номера страницы
    URL = driver.current_url
    URL_PARTS = (URL[:URL.find("page=") + 5], URL[URL.find("page=") + 6:])
    print(URL_PARTS)

    # создаём словарь для хранения неотсортированных результатов
    raw_results_list = {}

    # обходим все страницы
    for i in range(1, max_pages + 1):
        NEW_URL = str(i).join(URL_PARTS)
        driver.get(NEW_URL)

        # находим таблицу с результатами поиска
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.TAG_NAME, "app-goods-tile-default")))
        table = driver.find_elements(By.TAG_NAME, "app-goods-tile-default")

        for item in table:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "goods-tile__content")))
            item_name1 = item.find_element(By.CLASS_NAME, "goods-tile__content")
            name = item_name1.find_element(By.CLASS_NAME, "goods-tile__title")
            item_price = item.find_element(By.CLASS_NAME, "goods-tile__prices")
            price = int(item_price.text.split("\n")[-1].replace(" ", "").strip("₴"))
            if name in raw_results_list.keys():
                print("DUPLICATE NAME 0_0", price)
            raw_results_list[name.text] = price

        # сортируем результаты и пытаемся убрать ненужные
        results_list = {k: v for k, v in sorted(raw_results_list.items(), key=lambda kv: (kv[1], kv[0])) if
                        all(word in k.lower().split() for word in QUERY.lower().split())}


# except Exception as e:
#     print(e)

finally:
    driver.quit()

with open(QUERY + " results.json", "w", encoding='utf-8') as file:
    json.dump(results_list, file, ensure_ascii=False)
