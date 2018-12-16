

mysql
root/1234

SHOW DATABASES;
CREATE DATABASE test ;
DROP DATABASE shopping_db;
use test;

CREATE TABLE customer (id CHAR(10), name VARCHAR(10), age INT, ADDRESS VARCHAR(30));
INSERT  INTO customer  (id,name,age,address)  VALUES ( 'hong' ,'‘홍길동' , 22, '경기');
INSERT  INTO customer  VALUES ( 'kim', '김길동' , 26, '서울');

commit;


======================================================================
sqlite

G:\2019\python\python_work\Python_01\src\data>sqlite3 test.db
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.
sqlite> CREATE TABLE customer (id integer primary key autoincrement, name text not null, age integer, ADDRESS text);
sqlite> INSERT  INTO customer  (id,name,age,address)  VALUES ( 1 ,'‘홍길동' , 22, '경기');
sqlite> INSERT  INTO customer  VALUES ( 2, '김길동' , 26, '서울');
sqlite> .tables
customer
sqlite> .exit

G:\2019\python\python_work\Python_01\src\data>


=============================================================