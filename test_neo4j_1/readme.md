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





네, 복잡한 Neo4j 그래프 데이터베이스의 노드와 관계를 설계하는 예제를 만들어 드리겠습니다. 이 예제에서는 소셜 미디어 플랫폼을 모델링하고, CSV 파일을 이용하여 데이터를 삽입하는 Cypher 쿼리를 제공하겠습니다.

### 데이터 모델

1. **노드 타입**
   - `User`: 사용자를 나타냄. 속성으로 `userId`, `name`, `email`을 가짐.
   - `Post`: 게시물을 나타냄. 속성으로 `postId`, `content`, `createdAt`을 가짐.
   - `Tag`: 해시태그를 나타냄. 속성으로 `tagName`을 가짐.
   - `Topic`: 관심 주제를 나타냄. 속성으로 `topicName`을 가짐.

2. **관계 타입**
   - `FOLLOWS`: `User`가 다른 `User`를 팔로우함.
   - `POSTED`: `User`가 `Post`를 작성함.
   - `TAGGED_IN`: `Post`에 `Tag`가 포함됨.
   - `INTERESTED_IN`: `User`가 특정 `Topic`에 관심이 있음.

### CSV 파일 예시

1. **users.csv**
   ```
   userId,name,email
   1,Alice,alice@example.com
   2,Bob,bob@example.com
   3,Carol,carol@example.com
   ```

2. **posts.csv**
   ```
   postId,content,createdAt,userId
   101,First post,2023-01-01,1
   102,Hello World,2023-01-02,2
   103,Neo4j is awesome,2023-01-03,3
   ```

3. **tags.csv**
   ```
   tagName
   Neo4j
   Hello
   ```

4. **topics.csv**
   ```
   topicName
   GraphDatabases
   SocialMedia
   ```

### Cypher 쿼리 예시

1. **사용자 삽입**
   ```cypher
   LOAD CSV WITH HEADERS FROM 'file:///users.csv' AS

row
   CREATE (:User { userId: toInteger(row.userId), name: row.name, email: row.email })
   ```

2. **게시물 삽입**
   ```cypher
   LOAD CSV WITH HEADERS FROM 'file:///posts.csv' AS row
   MATCH (u:User { userId: toInteger(row.userId) })
   CREATE (p:Post { postId: toInteger(row.postId), content: row.content, createdAt: row.createdAt })
   CREATE (u)-[:POSTED]->(p)
   ```

3. **해시태그 삽입**
   ```cypher
   LOAD CSV WITH HEADERS FROM 'file:///tags.csv' AS row
   CREATE (:Tag { tagName: row.tagName })
   ```

4. **주제 삽입**
   ```cypher
   LOAD CSV WITH HEADERS FROM 'file:///topics.csv' AS row
   CREATE (:Topic { topicName: row.topicName })
   ```

5. **관계 설정**
   - 예를 들어, 특정 게시물에 해시태그를 태깅하는 쿼리:
     ```cypher
     MATCH (p:Post), (t:Tag)
     WHERE p.postId = 101 AND t.tagName = "Neo4j"
     CREATE (p)-[:TAGGED_IN]->(t)
     ```
   - 사용자 간의 팔로우 관계 설정:
     ```cypher
     MATCH (a:User), (b:User)
     WHERE a.userId = 1 AND b.userId = 2
     CREATE (a)-[:FOLLOWS]->(b)
     ```

6. **사용자가 관심 있는 주제 설정**
   ```cypher
   MATCH (u:User), (t:Topic)
   WHERE u.userId = 1 AND t.topicName = "GraphDatabases"
   CREATE (u)-[:INTERESTED_IN]->(t)
   ```

이 예제는 복잡한 소셜 미디어 플랫폼의 기본 구조를 나타내며, 실제로는 더 많은 노드, 속성, 관계를 포함할 수 있습니다. CSV 파일과 Cypher 쿼리는 이 예제의 구조에 따라 조정되어야 합니다. CSV 파일의 경로는 실제 파일이 저장된 경로에 따라 달라질 수 있습니다.