import streamlit as st
import re
from collections import Counter

st.markdown("<h1 style='text-align: center;'>Density Checker</h1>", unsafe_allow_html=True)
st.markdown("---")
text = st.text_area("Paragraph")
col1, col2, col3 = st.columns(3)
words_dict = dict()
if text:
    col1.markdown(f"<h3 style='text-align: center;'>Keywords</h3>", unsafe_allow_html=True)
    col2.markdown(f"<h3 style='text-align: center;'>Occurencies</h3>", unsafe_allow_html=True)
    col3.markdown(f"<h3 style='text-align: center;'>Pergentages</h3>", unsafe_allow_html=True)
    sim_text = re.sub("[.?!&*;:]", "", text)
    words = sim_text.lower()
    t_len = len(words)
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    keys = list(words_dict.keys())
    values = list(words_dict.values())
    for i in range(len(keys)):
        col1.markdown(F"<h5 style='text-align: center;'>{keys[i]}</h5>", unsafe_allow_html=True)
        col2.markdown(F"<h5 style='text-align: center;'>{values[i]}</h5>", unsafe_allow_html=True)
        col3.markdown(F"<h5 style='text-align: center;'>{(values[i] / t_len) * 100:.2f}%</h5>", unsafe_allow_html=True)

