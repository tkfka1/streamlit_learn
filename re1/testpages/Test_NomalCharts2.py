# 필요한 라이브러리를 불러옵니다.
import streamlit as st
import pandas as pd
import numpy as np

# Streamlit 앱의 제목을 설정합니다.
st.title('간단한 데이터 대시보드')

# 임의의 데이터를 생성합니다.
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

# Streamlit을 사용하여 데이터프레임을 화면에 표시합니다.
st.write("데이터 프레임:")
st.write(data)

# Streamlit을 사용하여 데이터의 히스토그램을 그립니다.
st.write("히스토그램:")
st.bar_chart(data)

# 데이터의 라인 차트를 그립니다.
st.write("라인 차트:")
st.line_chart(data)

# 슬라이더를 사용하여 그래프에 표시할 데이터의 수를 선택할 수 있습니다.
num_points = st.slider('포인트 수 선택', 5, 50)

# 선택된 수만큼의 데이터 포인트로 라인 차트를 그립니다.
st.write(f"선택된 데이터 포인트 ({num_points}개)로 라인 차트:")
st.line_chart(data.iloc[:num_points, :])
