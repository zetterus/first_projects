import requests
from bs4 import BeautifulSoup
import json
import schedule
import time

# WARNING!
print("WARNING!\n Frequent usage may cause block. Use at your own risk")

# параметры поиска
while True:
    try:
        tag_id = input(
            """Action (ID: 19)
Indie (ID: 492)
Adventure (ID: 21)
Casual (ID: 597)
RPG (ID: 122)
Strategy (ID: 9)
Simulation (ID: 599)
Early Access (ID: 493)
Free to Play (ID: 113)
Sports (ID: 701)
Enter game tag id:""")
        tag_id == int(tag_id)
        is_discounted = input("Search for discounted? 1 - yes, 0 - no")
        is_discounted in (0, 1)
        scheduled_time = input("Input check time(example 14:30):")
        0 < scheduled_time.split(":")[0] < 24
        0 < scheduled_time.split(":")[1] < 60
        print("Input accepted")
        break
    except:
        print("Invalid user.. input")


def watcher():
    # Начальный номер страницы
    page_number = 0
    page_count = 100  # Количество игр на одной странице, больше 100 не даёт?
    game_number = 1

    # Открываем файл в режиме записи, чтобы очистить его
    with open("watcher_report.txt", "w", encoding="utf-8") as file:
        pass

    # Открываем файл в режиме добавления
    with open("watcher_report.txt", "a", encoding="utf-8") as file:
        while True:
            # Формируем URL для каждой страницы
            url = f"https://store.steampowered.com/search/results/?query&start={page_number}&count={page_count}&dynamic_data=&sort_by=_ASC&tags={tag_id}&snr=1_7_7_2300_7&specials={is_discounted}&infinite=1"

            # Отправляем запрос на сервер
            response = requests.get(url)

            # Проверяем статус ответа
            if response.status_code == 200:
                print(f"page № {page_number} proceed")

                # Парсим JSON ответ
                data = json.loads(response.text)

                # Извлекаем HTML из ключа "results_html"
                results_html = data.get('results_html', '')

                # Если результатов нет, завершаем цикл
                if results_html == "\r\n<!-- List Items -->\r\n<!-- End List Items -->\r\n":
                    print("Конец результатов поиска")
                    break

                # Парсим HTML с помощью BeautifulSoup
                soup = BeautifulSoup(results_html, 'html.parser')
                games_list = soup.find_all("a", class_="search_result_row")

                for game in games_list:
                    game_name = game.find("span", class_="title").text
                    game_link = game.get("href")
                    try:
                        game_discount = game.find("div", class_="discount_pct").text
                        discount_original_price = game.find("div", class_="discount_original_price").text
                        discount_final_price = game.find("div", class_="discount_final_price").text
                        game_string = f"{game_number}. {game_name} discount: {game_discount} discounted price: {discount_final_price} original price: {discount_original_price}\n{game_link}\n"
                    except:
                        game_string = f"{game_number}. {game_name} discount: no discount info\n{game_link}\n"

                    game_number += 1
                    file.write(game_string)

                # Запись данных страницы в файл в режиме добавления
                file.write(f"\n\n=== Страница {page_number} ===\n\n")

                # Переходим к следующей странице
                page_number += page_count
            else:
                print(f"Ошибка запроса: {response.status_code}")
                break


schedule.every().day.at(scheduled_time).do(watcher)

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверять каждые 60 секунд
