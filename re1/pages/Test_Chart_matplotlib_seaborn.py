# styled_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data():
    """임의의 데이터 생성"""
    dates = pd.date_range('20210101', periods=100)
    data = pd.DataFrame(np.random.rand(100, 4), index=dates, columns=list('ABCD'))
    return data

def draw_stacked_bar_chart(data):
    """누적 막대 차트 그리기"""
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    data.cumsum().plot(kind='bar', stacked=True)
    plt.title("Stacked Bar Chart")
    plt.ylabel("Cumulative Sum")
    st.pyplot(plt)

def draw_line_chart(data):
    """선형 차트 그리기"""
    plt.figure(figsize=(10, 6))
    sns.set(style="darkgrid")
    sns.lineplot(data=data, dashes=False)
    plt.title("Line Chart")
    plt.ylabel("Value")
    st.pyplot(plt)

def main():
    st.title("Enhanced Charts Dashboard")

    data = generate_data()

    col1, col2 = st.columns(2)

    with col1:
        draw_stacked_bar_chart(data)

    with col2:
        draw_line_chart(data)

if __name__ == "__main__":
    main()
