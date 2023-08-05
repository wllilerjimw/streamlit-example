from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def propote(date):
    return "陈燕，嫁给我吧"


x= input("请输入我们的恋爱纪念日时间")
if x =="2021年6月8日":
   print(propote(x))
else:
    print("日期错误，请重新输入")

