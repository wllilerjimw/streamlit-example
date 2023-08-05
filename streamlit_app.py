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
import streamlit as st

def propose(date):
  return "陈燕,嫁给我吧"

if __name__ == '__main__':

    st.title("小惊喜哦，请年月日输清楚")
    
    date = st.text_input("请输入恋爱纪念日")  

    if date == "2021年6月8日":
        st.write(propose(date))
    else:
        st.write("日期错误,请重新输入")
