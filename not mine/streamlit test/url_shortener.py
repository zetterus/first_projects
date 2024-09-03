import streamlit as st
import pyshorteners as pyst
import pyperclip


def copying():
    pyperclip.copy(st.session_state.shorted_url)
    st.session_state.copied = True


shortener = pyst.Shortener()
st.markdown("<h1 style='text-align: center;'>URL SHORTENER</h1>", unsafe_allow_html=True)

# Используем сессионное состояние для хранения короткого URL и флага копирования
if "shorted_url" not in st.session_state:
    st.session_state.shorted_url = ""
if "copied" not in st.session_state:
    st.session_state.copied = False

form = st.form("name")
url = form.text_input("URL HERE")
s_btn = form.form_submit_button("SHORT")
if s_btn:
    st.session_state.shorted_url = shortener.tinyurl.short(url)
    st.session_state.copied = False  # Сброс флага после нового сокращения URL

if st.session_state.shorted_url:
    st.markdown("<h3 style='text-align: center;'>SHORTED URL</h3>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center;'>{st.session_state.shorted_url}</h6>", unsafe_allow_html=True)
    c_btn = st.button("Copy", on_click=copying)
    if st.session_state.copied:
        st.write("copied")
