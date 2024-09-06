import streamlit as st
import time


@st.cache_data
def printer():
    st.write("Running")
    time.sleep(3)
    return "Message"

st.write(printer())
