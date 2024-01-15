import streamlit as st

#mysql 라이브러리 import
import mysql.connector
from mysql.connector import Error 

def main():
    try :
        connection = mysql.connector.connect(
            host = '1',
            database = 'testdb',
            user = 'hankyo',
            password = '1'
        )

		#커넥션을 제대로 가져왔을 경우 이 부분이 실행된다.
        if connection.is_connected() :
        
        	#커서를 가져온다.
            cursor = connection.cursor(dictionary= True)
            
            #실행할 쿼리문을 작성하면,
            query = """ select *
                        from books limit 5; """
                        
            #이 부분에서 쿼리를 실행해준다.
            #쿼리를 여러개 실행할 땐, executemany라는 함수를 사용할 수 있다.
            cursor.execute(query)
            
            #그리고 쿼리 실행의 결과를 가져와, results라는 변수에 저장한 것이다.
            #fetchall일 경우 결과를 모두 가져오고, fetchone일 경우 하나만 가져온다.
            results = cursor.fetchall()

			#이 부분은 스트림릿 앱 화면에 보여주기 위해 작성된 부분이다.
            #그냥 print로 results만 찍어봐도 터미널에 결과가 찍힌다.
            for row in results :
                st.write(row)
                book_id_list.append( row['book_id'] )

	#DB 관련 에러가 발생할 시, 터미널에 에러 문구를 출력하게 했다.
    except Error as e :
            print('디비 관련 에러 발생', e)
    
    #마지막엔 커서와 커넥션을 닫아준다.
    #닫아주지 않을 경우 뒤에서 또 커서와 커넥션을 사용하게 됐을 때 제대로 작동하지 않을 수 있다.
    finally :
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")


if __name__ == '__main__':
    main()