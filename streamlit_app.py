from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome my baby!

这是一份惊喜，请输入正确日期，你便能看到哦！
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
