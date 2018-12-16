# MySQL tyy catch

import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='test', charset='utf8')
 
try:
    # INSERT
    with conn.cursor() as curs:
        sql = "insert into customer(id,name,age,address) values (%s, %s, %s, %s)"
        curs.execute(sql, ('uer01','이광수', 22, '서울'))
 
    conn.commit()
 
    # SELECT
    with conn.cursor() as curs:
        sql = "select * FROM customer"
        curs.execute(sql)
        rs = curs.fetchall()
        for row in rs:
            print(row)
 
finally:
    conn.close()

# INSERT와 SELECT 문을 각기 다른 커서에서 사용하고 있다. 
# 첫번째 INSERT 실행 시 with 문으로 커서를 만들어 자동으로 커서 리소스가 해제되도록 하였고, 
# 두번째 SELECT 시에도 with 문으로 해당 커서가 자동 해제    
