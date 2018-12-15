#Dictionary (dict)
#Dictionary는 "키(Key) - 값(Value)" 쌍을 요소로 갖는 컬렉션이다.
#Dictionary는 흔히 Map 이라고도 불리우는데, 키(Key)로 신속하게 값(Value)을 찾아내는 해시테이블(Hash Table) 구조

scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores["민수"]   # 특정 요소 읽기
scores["민수"] = 88  # 쓰기
print(scores)
print(v,'  ',scores["민수"])

print()
# 1. Tuple List로부터 dict 생성
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)
 
age = mydict["홍대길"]
print(age)   # 35
 
# 2. Key=Value 파라미터로부터 dict 생성
scores = dict(kim=80, hong=90, kang=85)
print(scores['kim'])  #90
#print(scores['KIM'])  key error 
print()
scores = {"철수": 90, "민수": 85, "영희": 80}
scores["민수"] = 88   # 수정
scores["길동"] = 95   # 추가
del scores["영희"]
print(scores)    # 출력 {'철수': 90, '길동': 95, '민수': 88}

for key in scores:
    val = scores[key]
    print("%s : %d" % (key, val))


scores = {"철수": 90, "민수": 85, "영희": 80}
 
# keys
keys = scores.keys()
for k in keys:
    print(k)
 
# values
values = scores.values()
for v in values:
    print(v)
print()
users = {"user01": '010-7777-1234', "user02": '010-9324-3333', "user03": '010-3578-9300'}
 
items = users.items()
print(items)
# 출력: dict_items([('user01', '010-7777-1234'), ('user02', '010-9324-3333'), ('user03', '010-3578-9300')])
# =>    [('user01', '010-7777-1234'), ('user02', '010-9324-3333'), ('user03', '010-3578-9300')] 
# dict_items를 리스트로 변환할 때
itemsList = list(items)    
print(itemsList)
print(users['user01'])
for id in users:
    print("ID:%s ,Phone Number : %s" % (id, users[id]))

print()
scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores.get("민수")  # 85
v = scores.get("길동")  # None
#v = scores["길동"]      # 에러 발생
 
# 멤버쉽연산자 in 사용
if "길동" in scores:
    print(scores["길동"])
 
scores.clear()  # 모두 삭제
print(scores)
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)
 
mydict.update({'홍대길':33,'강찬수':26})

