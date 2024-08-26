import streamlit as st
from datetime import date
from datetime import timedelta as td
from datetime import time as ti
import time
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# #remove streamlit hamburger (& any other elements)
# st.markdown("""
# <style>
# .st-emotion-cache-yfhhig.ef3psqc5
# {
# visibility: hidden;
# }
# </style>
# """, unsafe_allow_html=True)
# # completely removes header
# # .st-emotion-cache-h4xjwg.ezrtsby2
# # {
# # visibility: hidden;
# # }

#
# # text elements
# st.title("Title")
# st.subheader("Subhead")
# st.header("Header")
# st.text("Text")
# st.markdown(":orange[**Hello** >world :sunglasses:]", help="markdown test")
# st.markdown("""1. Hello
# 2. cruel
# 3. world""")
# st.markdown("""- Hello
# - cruel
# - world""")
# st.markdown("`steamlit is op`")
# st.markdown("---")
# st.markdown("[title](https://www.example.com)")
# st.caption("This is caption")
# st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
# st.latex(r"\cfrac{a}{1 + \cfrac{1}{b}}\sqrt[3]{x}")
# st.latex(r"\displaystyle\sum_{i=1}^n")
# json = {"a": "1, 2, 3", "b": "4, 5, 6"}
# st.json(json)
# code = """
# print("code example")
# def func():
#     return 0"""
# st.code(code, language="python")
# st.write("## H2")
# st.metric(label="Wind speed", value="120m/s", delta="-1.4m/s", delta_color="inverse", help="help text", label_visibility="visible")
#
# # dataframe
# label = pd.DataFrame({"column_1": [1,2,3,4,5,6,7], "column_2":[11,12,13,14,15,16,17]})
# st.table(label)
# st.dataframe(label)
#
# # media
# st.image("not mine/streamlit test/1.jpg", caption="caption example", width=400)
# st.audio("not mine/streamlit test/look!.mp3")
# st.video("not mine/streamlit test/Еб рот вместо тысячи слов.mp4")
#
# # interactive widgets
# def change():
#     print(st.session_state)
# state = st.checkbox("checkbox", value=True, on_change=change)
# if state:
#     st.write("Hi")
# else:
#     pass
# radio_btn = st.radio("question", options=(1, 2, 3), index=2, help="help text", horizontal=True, captions=("a", "b", "c"))
# st.write(radio_btn)
# btn = st.button("button example", on_click=lambda: st.write("button clicked"))
# select = st.selectbox("question2", options=(1, 2, 3))
# st.write(select)
# multiselect = st.multiselect("question3", options=(1, 2, 3))
# st.write(multiselect)

# # upload files and display them
# st.title("Upload your file, mortal.")
# st.markdown("---")
# allowed = ["png", "jpg", "txt", "mp3"]
# files = st.file_uploader("NOW!", accept_multiple_files=True)
#
# if files:
#     for file in files:
#         file_extension = file.name.split('.')[-1].lower()  # Получаем расширение файла
#
#         if file_extension in ["png", "jpg", "jpeg"]:
#             st.image(file)
#         elif file_extension == "mp3":
#             st.audio(file)
#         elif file_extension == "mp4":
#             st.video(file)
#         elif file_extension == "txt":
#             content = file.read().decode("utf-8")
#             st.text(content)
#         else:
#             st.write("Unsupported format, fool")

# # sliders
# val = st.slider("slider example", min_value=4, max_value=42, value=8)
# st.write(val)
# val2 = st.text_input("enter text", max_chars=3)
# st.write(val2)
# val3 = st.text_area("enter text2", max_chars=10)
# st.write(val3)
# val4 = st.date_input("enter date", min_value=date(1980, 1, 1))
# st.write(val4)
#
#
# # timer
# def convert(t):
#     m, s, ms = t.split(":")
#     t_s = int(m) * 60 + int(s) + int(ms) / 1000
#     return t_s
#
#
# val5 = st.time_input("timer name", value=ti(0, 0, 0), step=td(seconds=60))
# st.write(val5)
# if str(val5) == "00:00:00":
#     st.write("set the timer!")
# else:
#     sec = convert(str(val5))
#     bar = st.progress(0)
#     per = sec / 100
#     status = st.empty()
#     for i in range(100):
#         bar.progress(i + 1)
#         status.write(F"{i}%")
#         time.sleep(per)

# # forms
# st.markdown("<h1 style='text-align: center;'>User registration</h1>", unsafe_allow_html=True)
# form = st.form("form 1")
# form.text_input("First Name")
# form.form_submit_button("Submit")
#
# with st.form("form 2", clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     s_name = col1.text_input("Second name")
#     l_name = col2.text_input("Last name")
#     st.text_input("Email Address")
#     st.text_input("Password")
#     st.text_input("Confirm Password")
#     day, month, year = st.columns(3)
#     day.text_input("Day")
#     month.text_input("Month")
#     year.text_input("Year")
#     s_state = st.form_submit_button("Submit registration")
#     if s_state:
#         if s_name == "" and l_name == "":
#             st.warning("Please fill above fields")
#         else:
#             st.success("Submitted successfully")


# sidebar
x = np.linspace(0, 10, 100)
bar_x = np.array([1, 2, 3, 4, 5])

# st.sidebar.write("this is sidebar")
# fig = plt.figure()
# plt.plot(x, np.sin(x))
# st.write(fig)

opt = st.sidebar.radio("select graph", options=("line", "bar", "h-bar"))
if opt == "line":
    st.markdown("<h1 style='text-align: center;'>line chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    # plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    st.write(fig)
elif opt == "bar":
    st.markdown("<h1 style='text-align: center;'>line chart</h1>", unsafe_allow_html=True)
    fig2 = plt.figure()
    plt.bar(bar_x, bar_x * 10)
    st.write(fig2)
else:
    st.markdown("<h1 style='text-align: center;'>line chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.barh(bar_x*10, bar_x)
    st.write(fig)



# decorations
# st.snow()
