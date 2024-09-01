import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

from PIL import Image
from io import BytesIO

st.set_page_config(page_title="semi-scrapper", page_icon=":flushed:", layout="wide",
                   menu_items={
                       'Get Help': 'https://www.extremelycoolapp.com/help',
                       'Report a bug': "https://www.extremelycoolapp.com/bug",
                       'About': "# This is a header. This is an *extremely* cool app!"
                   }
                   )

st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")
placeholder = st.empty()
if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}") # https://unsplash.com/napi/search/photos?page=2&per_page=20&query={keyword}&xp=search-disable-synonyms-2%3Aexperiment
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class_="LYMM9")
    col1, col2 = placeholder.columns(2)
    figures = rows[0].find_all("figure")
    i = 0
    for index, figure in enumerate(figures):
        img = figure.find("img", class_="I7OuT DVW3V L1BOa")
        image = img["src"].split("?")[0]
        anchor = figure.find("a", class_="zNNw1")
        if i == 0:
            i = 1
            col1.image(image)
            # btn = col1.button("Download", key=str(index) + str(i))
            col1.write(image)
            # if btn:
            #     response = requests.get(image)
            #     img = Image.open(BytesIO(response.content))
        else:
            i = 0
            col2.image(image)
            # btn = col2.button("Download", key=str(index) + str(i))
            col2.write(image)
            # if btn:
            #     response = requests.get(image)
            #     img = Image.open(BytesIO(response.content))
