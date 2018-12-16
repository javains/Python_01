#  Python DB API는 여러 데이타베이스를 엑세스하는 표준 API 
#  표준 API는 크게 데이타베이스를 연결하고, SQL 문을 실행하고, 연결을 닫는 등의 기본적인 DB 작업과 관련된 기능들을 정의

#  MySQL   ->  pip install PyMySQL

# . MySql 사용 절차
# PyMySql 모듈을 import 한다  =>  import pymysql
# pymysql.connect() 메소드를 사용하여 MySQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정한다.
# DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다. DB 커서는 Fetch 동작을 관리하는데 사용되는데, 만약 DB 자체가 커서를 지원하지 않으면, Python DB API에서 이 커서 동작을 Emulation 하게 된다.
# Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다.
# SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용한다.
# 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이타를 확정 갱신한다.
# Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.

import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='test', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from customer"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 row들을 Tuple
print(rows[0])  
print(rows[1])  
 
# Connection 닫기
conn.close()

###########################
print()
import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='test', charset='utf8')
 
# Connection 으로부터 Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)
 
# SQL문 실행
sql = "select * from customer where id=%s and name=%s"
curs.execute(sql, ('kim', '김길동'))
 
# 데이타 Fetch
rows = curs.fetchall()  
for row in rows:
    print(row)
    print(row['id'], row['name'], row['ADDRESS'])   # 대소문자구분
# Row 데이타가 Dictionary이므로 row["id"], row["name"] 
# Connection 닫기
conn.close()

# fetchall()
# fetchone()
# fetchmany(n)





# mysql
# root/1234

# SHOW DATABASES;
# CREATE DATABASE test ;
# DROP DATABASE shopping_db;
# use test;

# 
# CREATE TABLE customer (id CHAR(10), name VARCHAR(30), age INT, ADDRESS VARCHAR(30));
# INSERT  INTO customer  (id,name,age,address)  VALUES ( 'hong' ,'‘홍길동' , 22, '경기');
# INSERT  INTO customer  VALUES ( 'kim', '김길동' , 26, '서울');

# commit;