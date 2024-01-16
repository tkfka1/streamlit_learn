from neo4j import GraphDatabase

uri = "neo4j+s://123.databases.neo4j.io"  # Neo4j 인스턴스의 URI
username = "neo4j"  # 사용자 이름
password = "123"  # 비밀번호

driver = GraphDatabase.driver(uri, auth=(username, password))

def get_data(query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]
