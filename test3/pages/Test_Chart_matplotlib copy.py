import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data():
    """임의의 데이터 생성"""
    dates = pd.date_range('20210101', periods=100)
    data = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=list('ABCD'))
    return data


def draw_chart(data, chart_type, title):
    """주어진 데이터와 차트 유형을 사용하여 차트 그리기"""
    fig, ax = plt.subplots()
    
    # 데이터를 양수로 변환
    if chart_type == "area":
        data = data.abs()

    if chart_type == "line":
        data.plot(ax=ax)
    elif chart_type == "bar":
        data.sum().plot.bar(ax=ax)
    elif chart_type == "box":
        data.plot.box(ax=ax)
    elif chart_type == "hist":
        data.plot.hist(bins=20, ax=ax)
    elif chart_type == "kde":
        data.plot.kde(ax=ax)
    elif chart_type == "area":
        data.plot.area(ax=ax)

    st.write(title)
    st.pyplot(fig)

def main():
    st.title("Multi-Chart Dashboard")

    data = generate_data()

    # 2열 3행의 그리드 생성
    col1, col2 = st.columns(2)

    with col1:
        draw_chart(data, "line", "Line Chart")
        draw_chart(data, "bar", "Bar Chart")
        draw_chart(data, "box", "Box Plot")

    with col2:
        draw_chart(data, "hist", "Histogram")
        draw_chart(data, "kde", "Kernel Density Estimate")
        draw_chart(data, "area", "Area Chart")

if __name__ == "__main__":
    main()