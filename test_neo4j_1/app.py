from neo4j import GraphDatabase
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Neo4j 데이터베이스 연결 설정
uri = "neo4j+s://7.databases.neo4j.io"  # Neo4j 인스턴스의 URI
username = "neo4j"  # 사용자 이름
password = "1"  # 비밀번호
auth = (username, password)
# driver = GraphDatabase.driver(uri, auth=(username, password))

# # 데이터 검색 함수
# def get_data(query):
#     with driver.session() as session:
#         result = session.run(query)
#     return [record for record in result]

# 데이터 검색 쿼리
query = """
MATCH (n)-[r]->(m)
RETURN n, r, m
"""

# 데이터 검색
# data = get_data(query)

with GraphDatabase.driver(uri, auth=auth) as driver:
    driver.verify_connectivity()


with GraphDatabase.driver(uri, auth=auth) as driver:
    result = driver.session().run(query)
    print(result)
    print([record for record in result])

# # 데이터 프레임으로 변환
# df = pd.DataFrame(data, columns=['date', 'sales'])

# # Streamlit 대시보드
# st.title('일별 매출 시각화')
# st.bar_chart(df.set_index('date'))
