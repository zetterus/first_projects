import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")
placeholder = st.empty()
if search:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class_="bugb2")
    col1, col2 = placeholder.columns(2)
    for row in rows:
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img", class_="I7OuT DVW3V L1BOa")
            image = img["src"].split("?")[0]
            if i == 0:
                col1.image(image)
            else:
                col2.image(image)



