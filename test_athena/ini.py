import unittest
from unittest.mock import patch
from my_module import execute_athena_query  # 가정: 위 함수가 my_module에 있다

class TestAthenaQuery(unittest.TestCase):

    @patch('my_module.boto3.client')
    def test_execute_athena_query(self, mock_client):
        # Mock 객체 설정
        mock_response = {
            'QueryExecution': {
                'Status': {'State': 'SUCCEEDED'}
            },
            'ResultSet': {
                'Rows': [
                    {'Data': ['Column1', 'Column2']},
                    {'Data': ['Value1', 'Value2']}
                ]
            }
        }
        mock_client.return_value.get_query_execution.return_value = mock_response
        mock_client.return_value.get_query_results.return_value = mock_response

        # 쿼리 실행
        result = execute_athena_query("SELECT * FROM my_table", "my_database")

        # 예상 결과 검증
        expected_result = pd.DataFrame([['Column1', 'Column2'], ['Value1', 'Value2']])
        pd.testing.assert_frame_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()
