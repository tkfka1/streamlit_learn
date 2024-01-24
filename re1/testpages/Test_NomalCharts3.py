# 필요한 라이브러리를 불러옵니다.
import streamlit as st
import pandas as pd
import numpy as np

# Streamlit 앱의 제목을 설정합니다.
st.title('체크박스를 사용한 데이터 선택 대시보드')

# 임의의 데이터를 생성합니다.
data = pd.DataFrame(
    np.random.randn(100, 4),
    columns=['A', 'B', 'C', 'D']
)

# Streamlit을 사용하여 데이터프레임을 화면에 표시합니다.
st.write("데이터 프레임:")
st.write(data)

# 각 열에 대한 체크박스를 생성합니다.
selected_columns = []
for column in data.columns:
    if st.checkbox(f'{column} 열 보기', value=True):
        selected_columns.append(column)

# 선택된 열만 포함하는 데이터프레임을 생성합니다.
selected_data = data[selected_columns]

# 선택된 데이터의 라인 차트를 그립니다.
st.line_chart(selected_data)
