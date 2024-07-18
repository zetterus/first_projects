from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

URL = "https://rozetka.com.ua/"
PATH = "D:\\python\\first_projects\\not mine\\scraping\\Tech with Tim\\chromedriver.exe"
QUERY = "asus rog"  # input("VVODI ZAPROS")

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get(URL)

try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.NAME, "search")))
    search = driver.find_element(By.NAME, "search")
    search.send_keys(QUERY)
    search.send_keys(Keys.ENTER)

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, "app-goods-tile-default")))
    table = driver.find_elements(By.TAG_NAME, "app-goods-tile-default")

    # items = table.find_elements()
    for item in table:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "goods-tile__content")))
        item_name1 = item.find_element(By.CLASS_NAME, "goods-tile__content")
        item_name2 = item_name1.find_element(By.CLASS_NAME, "goods-tile__title")
        old_item_price = item.find_element(By.CLASS_NAME, "goods-tile__prices")
        # new_item_price = item.find_element(By.CLASS_NAME, "goods-tile__price-value")
        print(item_name2.text, old_item_price.text.split("\n"))  # ну и как этой хероты достать прицельно текст конкретного тага?!
        print()

    # items = table.find_elements(By.CLASS_NAME, "product-link goods-tile__heading")
    # print(items)

finally:
    driver.quit()
