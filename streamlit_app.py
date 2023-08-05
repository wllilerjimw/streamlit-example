from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
import streamlit as st

# BMI计算函数
def calculate_bmi(height, weight):
  bmi = weight / (height ** 2)
  if bmi < 18.5:
    return "过轻"
  elif bmi < 25:
    return "正常"
  elif bmi < 28:
    return "过重"
  elif bmi < 32:
    return "肥胖"
  else:
    return "严重肥胖"

# 主函数  
if __name__ == '__main__':

  st.title("小惊喜哦,请年月日输清楚")

  date = st.text_input("请输入恋爱纪念日")

  if date == "2021年6月8日":
    st.write("陈燕,嫁给我吧")

  else:
    st.write("日期错误,请重新输入")
    

