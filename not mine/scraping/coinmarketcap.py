from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs:
    name, price = tr.contents[2:4]
    find_name = name.find_all(["p", "span"])
    if len(find_name) == 2:
        fixed_name = find_name[0].text
    elif len(find_name) == 3:
        fixed_name = find_name[1].text
    fixed_price = price.text

    prices[fixed_name] = fixed_price

print(prices)
print(len(prices))
