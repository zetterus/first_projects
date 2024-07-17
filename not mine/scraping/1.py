import os
import requests
from bs4 import BeautifulSoup

url = "https://commons.wikimedia.org/wiki/List_of_dog_breeds"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "wikitable sortable"})

    names = []
    groups = []
    local_names = []
    photographs = []

    os.makedirs("dog_images", exist_ok=True)

    for row in table.find_all("tr")[1:]:
        columns = row.find_all(["td", "th"])

        name = columns[0].find("a").text.strip()
        group = columns[1].text.strip()

        span_tag = columns[2].find("span")
        local_name = span_tag.text.strip() if span_tag else ""

        img_tag = columns[3].find("img")
        photograph = img_tag["src"] if img_tag else ""

        if photograph:

            response = requests.get(photograph)

            if response.status_code == 200:

                image_filename = os.path.join("dog_images", f"{name}.jpg")

                with open(image_filename, "wb") as img_file:

                    img_file.write(response.content)

        names.append(name)
        groups.append(group)
        local_names.append(local_name)
        photographs.append(photograph)


print(names)
print(groups)
print(local_names)
print(photographs)

