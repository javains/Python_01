#Set
#Set은 중복이 없는 요소들 (unique elements)로만 구성된 집합 컬렉션이다.
#리스트나 튜플 등을 set으로 변경하기 위해서는 set() 생성자를 사용한다. 

# set 정의
myset = { 1, 1, 3, 5, 5 }
print(myset)    # 출력: {1, 3, 5}
 
# 리스트를 set으로 변환
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)        # 출력: {'A', 'B'}
print()

myset = {1, 3, 5}
 # 하나만 추가
myset.add(7)
print(myset)
 
# 여러 개 추가
myset.update({4,2,10})
print(myset)
 
# 하나만 삭제
myset.remove(1)
print(myset)
 
# 모두 삭제
myset.clear()
print(myset)
print()
# 집합 연산
a = {1, 3, 5}
b = {1, 2, 5}
 
# 교집합
i = a & b
# i = a.intersection(b)
print(i)   #{1, 5}
 
# 합집합
u = a | b
# u = a.union(b)
print(u)  #{1, 2, 3, 5}
 
# 차집합
d = a - b
# d = a.difference(b)
print(d)   #{3}

