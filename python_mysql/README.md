# 파이썬 mysql 연동하기


1) MYSQL 서버 설치
# apt-get install mysql-server

2) MYSQL 서버 서비스 시작
# service mysql start

3) root 패스워드 설정 ( 초기에는 비번이 없음 )
# mysql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '패스워드';
mysql> flush privileges;

4) 사용할 데이터베이스 생성 ( 데이터베이스명을 cray7db 로 정했으나 자유롭게 정해주셔도 됩니다 )
mysql> create database cray7db DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

5) cray7db 에 접근할 MYSQL 계정 추가 ( root 계정은 해킹당하면 심각하므로 보통 이 방식으로 계정을 추가하는게 좋습니다. 여기서는 cray7로 정하였으나 자유롭게 정해주셔도 됩니다.)

mysql> create user cray7@localhost identified by '추가계정비번'; # 로컬 오픈

6) cray7db 데이터베이스를 사용할 권한을 줍니다.
mysql> grant all privileges on cray7db.* to 'cray7'@'localhost' identified by '추가계정비번';

7) 외부에서 접속이 들어올 경우에도 접근 권한을 부여합니다. ( 사무실 내에서만 접속을 제한하려면 아래 본문 중 '보안을 더욱 확실히 하려면'을 참조하세요 )
mysql> grant all privileges on cray7db.* to 'cray7'@'%' identified by '추가계정비번';

8) 지정한 권한을 반영합니다.
mysql> flush privileges;
mysql> quit

패스워드에 의한 외부 접속 오픈

※ 이 이하는 mysql을 SQLyog와 같은 프로그램으로 외부에서 접속할 경우 해당하며, 외부 오픈하지 않을 경우 설정하지 않아도 무방합니다.

9) 서버 안쪽에서 외부 접속 오픈

 vi 에디터로 설정 파일을 연 다음,

# vi /etc/mysql/mysql.conf.d/mysqld.cnf

bind-address 127.0.0.1 라고 된 곳을 찾아
아래와 같이 앞에 #을 붙여 주석처리하고 저장합니다.
#bind-address ...



https://gradient-descent.tistory.com/46