# failed due to another site and events >:o

from bs4 import BeautifulSoup
import requests
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"
]

search_term = "asus rog"  # input("What product do you want to search for? ")

headers = {"User-Agent": random.choice(user_agents)}

url = f"https://rozetka.com.ua/search/?page={1}&text={search_term}"
page = requests.get(url, headers=headers).text
doc = BeautifulSoup(page, "lxml")

tag = doc.find_all()

print(doc)

# page_num = 0
#
# while True:
#     try:
#         page_num += 1
#         url = f"https://rozetka.com.ua/search/?page={page_num}&text={search_term}"
#         page = requests.get(url, headers=headers).text
#         doc = BeautifulSoup(page, "html.parser")
#
#         print(doc)
#     except:
#         break


# for page in range(1, max_pages_number + 1):
#     url = f"https://www.moyo.ua/ua/search/new/?q={"+".join(search_term.split())}&page={page}"
#     page = requests.get(url, headers=headers).text
#     doc = BeautifulSoup(page, "html.parser")
#
#     div = doc.find(class_="search_products js-products-list")
#     print(div)
#     print(1311)
#     items = div.find_all(class_="product-card goods-item add-data ga-item has-additional-data has-second-image")
#     print(items)

    # for item in div:
    #     print(item)
    #     print(1311)
    #     name = item.find_all("product-card_title gtm-link-product")
    #     price = item.find_all("product-card_price_current not-available")
    #     print(name, price)

