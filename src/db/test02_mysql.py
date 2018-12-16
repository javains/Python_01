# MySQL DML

import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='test', charset='utf8')
 
curs = conn.cursor()
sql = """insert into customer(id,name,age,address)
         values (%s, %s, %s, %s)"""
#curs.execute(sql, ('java01', '홍길동', 23, '서울'))
# curs.execute(sql, ('java02','이연수', 31, '서울'))
# conn.commit()
# conn.close()
 
data = (
    ('java03','홍진우', 19, '서울'),
    ('java04','강지수', 22, '부산'),
    ('java05','김청진', 11, '서울'),
)
# curs.executemany(sql, data)
conn.commit()


# UPDATE, DELETE 문
import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='test', charset='utf8')
 
curs = conn.cursor()
sql = """update customer
         set address = '서울특별시'
         where address = '서울'"""
curs.execute(sql)
 
sql = "delete from customer where id=%s"
curs.execute(sql, 'java04')
 
conn.commit()
conn.close()

