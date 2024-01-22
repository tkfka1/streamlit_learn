import boto3
import pandas as pd

def execute_athena_query(query, database):
    client = boto3.client('athena')
    
    # Athena 쿼리 실행
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': 's3://your-athena-results-bucket/path/'
        }
    )
    query_execution_id = response['QueryExecutionId']

    # 쿼리 결과가 준비될 때까지 기다림
    while True:
        response = client.get_query_execution(QueryExecutionId=query_execution_id)
        if response['QueryExecution']['Status']['State'] in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break

    # 쿼리 결과 가져오기
    results = client.get_query_results(QueryExecutionId=query_execution_id)
    # 결과를 DataFrame으로 변환
    return pd.DataFrame([r['Data'] for r in results['ResultSet']['Rows']])
