#Tuple
#Immutable 데이타 타입

t = ("AB", 10, False)
print(t)

t1 = (123)   #123  int 타입
print(t1)   

t2 = (123,)  #(123)  tuple 타입
print(t2)   

t = (1, 5, 10)
# 인덱스
second = t[1]      # 5
last = t[-1]       # 10
 
# 슬라이스
s = t[1:2]         # (5)
s = t[1:]          # (5, 10)

# 병합
a = (1, 2)
b = (3, 4, 5)
c = a + b
print(c)   # (1, 2, 3, 4, 5)
 
# 반복
d = a * 3  # 혹은 "d = 3 * a" 도 동일
print(d)   # (1, 2, 1, 2, 1, 2)

#Tuple 변수 할당
name = ("John", "Kim")
print(name)
# 출력: ('John', 'Kim')
 
firstname, lastname = ("John", "Kim")
print(lastname, ",", firstname)
# 출력: Kim, John


