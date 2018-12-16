# JSON  -> JavaScript Object Notation
# Python 타입의 Object를 JSON 문자열로 변경할 수 있으며(JSON 인코딩), 
# JSON 문자열을 다시 Python 타입으로 변환할 수 있다 (JSON 디코딩).
# JSON 포맷은 Key-Value Pair의 컬렉션이다.
# import json 

import json
 
# 테스트용 Python Dictionary
customer = {
    'id': 2018001,
    'name': '홍길동',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
print(type(customer) )  # <class 'dict'>
print(customer) 
# JSON 인코딩
jsonString = json.dumps(customer,indent=4)
print(type(jsonString) )  # <class 'str'>

# 문자열 출력
print(jsonString)
print(type(jsonString)) 

# JSON 디코딩
import json
 
# 테스트용 JSON 문자열
jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
print('*'*50)

# JSON 디코딩
dict = json.loads(jsonString)
# Dictionary 데이타 체크
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])