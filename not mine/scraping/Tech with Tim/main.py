from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="../../../chromedriver.exe")  # выбор драйвера?
driver = webdriver.Chrome(service=service)  # создание объекта?

driver.get("https://google.com")  # запрос к сайту(с помощью драйвера?)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)  # ждём 5 секунд, чтобы загрузился элемент, в даннос случае поле поиска, если не загрузится рушим(?) программу

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")  # поиск элемента по имени класса
input_element.clear()  # очистка поля
input_element.send_keys("tech with tim" + Keys.ENTER)  # ввод строки в найденное поле

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)  # ждём 5 секунд, чтобы загрузился элемент, в даннос случае поле поиска, если не загрузится рушим(?) программу

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

time.sleep(5)

driver.quit()  # закрытие браузера

