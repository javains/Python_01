# SQLite  -> Embedded SQL DB 엔진
# http://www.sqlite.org   -> sqlite-tools-win32-x86-3260000.zip

import sqlite3
 
# SQLite DB 연결
conn = sqlite3.connect("../data/test.db")
 
# Connection 으로부터 Cursor 생성
cur = conn.cursor()
 
# SQL 쿼리 실행
cur.execute("select * from customer")
 
# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
    print(row)
 
# Connection 닫기
conn.close()

##################################
print()
import sqlite3
 
conn = sqlite3.connect("../data/test.db")
 
cur = conn.cursor()
sql = "select * from customer where id=? and address=?"
cur.execute(sql, (2, '서울'))
rows = cur.fetchall()
for row in rows:
    print(row)
 
conn.close()
##################################
print()
# Named Placeholder
conn = sqlite3.connect("../data/test.db")
 
cur = conn.cursor()
sql = "select * from customer where id = :Id"
cur.execute(sql, {"Id": 1})
rows = cur.fetchall()
for row in rows:
    print(row)
 
conn.close()

# DML (INSERT, UPDATE, DELETE)
conn = sqlite3.connect("../data/test.db")
cur = conn.cursor()
sql = "insert into customer(name,age,address) values (?,?, ?)"
cur.execute(sql, ('고길동', 31, '서울'))
conn.commit()
conn.close()
#################################################3
import sqlite3
 
conn = sqlite3.connect("../data/test.db")
cur = conn.cursor()
 
data = (
    ('홍진우', 11, '서울'),
    ('강지수', 21, '부산'),
    ('김청진', 21, '서울'),
)
sql = "insert into customer(name,age,address) values (?, ?, ?)"
cur.executemany(sql, data)
 
conn.commit()
conn.close()

##########################################
print()
import sqlite3
 
conn = sqlite3.connect("../data/test.db")
 
with conn:
    cur = conn.cursor()
    cur.execute("select * from customer")
    rows = cur.fetchall()
 
    for row in rows:
        print(row)




# CREATE TABLE customer (id integer primary key autoincrement, name text not null, age integer, ADDRESS text);
# INSERT  INTO customer  (id,name,age,address)  VALUES ( 1 ,'‘홍길동' , 22, '경기');
# INSERT  INTO customer  VALUES ( 2, '김길동' , 26, '서울');