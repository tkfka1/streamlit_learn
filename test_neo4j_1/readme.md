1. Neo4j 데이터베이스 설정
기본 데이터 모델
노드: Product (상품), Order (주문)
관계: CONTAINS (포함)
샘플 데이터 생성
먼저, Neo4j의 Cypher 쿼리 언어를 사용하여 샘플 데이터를 생성합니다.

cypher
Copy code
// 상품 생성
CREATE (p1:Product {id: 1, name: '상품 A', price: 1000})
CREATE (p2:Product {id: 2, name: '상품 B', price: 2000})
CREATE (p3:Product {id: 3, name: '상품 C', price: 3000})

// 주문 생성 및 상품과 관계 설정
CREATE (o1:Order {id: 1, date: '2024-01-10', totalAmount: 5000})
CREATE (o2:Order {id: 2, date: '2024-01-15', totalAmount: 3000})
CREATE (o1)-[:CONTAINS]->(p1)
CREATE (o1)-[:CONTAINS]->(p2)
CREATE (o2)-[:CONTAINS]->(p3)

2. Python과 Streamlit을 사용한 데이터 시각화
필요한 라이브러리 설치
bash
Copy code
pip install neo4j pandas matplotlib streamlit