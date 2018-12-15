#List
#파이썬의 리스트는 동적배열(Dynamic Array)
#값을 자유롭게 변경할 수 있는 Mutable 데이타 타입
a = []     # 빈 리스트
a = ["AB", 10, False]

a = ["AB", 10, False]
x = a[1]        # a의 두번째 요소 읽기
a[1] = "Test"   # a의 두번째 요소 변경
y = a[-1]       # False

a = [1, 3, 5, 7, 10]
x = a[1:3]     # [3, 5]
x = a[:2]      # [1, 3]
x = a[3:]      # [7, 10]

print(a[1:3])
print(a[3:])
print(a[:2])

a = ["AB", 10, False]
a.append(21.5)  # 추가
a[1] = 11       # 변경
del a[2]        # False 삭제
print(a)        # ['AB', 11, 21.5]
print()
# 병합
a = [1, 2]
b = [3, 4, 5]
c = a + b
print(c)   # [1, 2, 3, 4, 5]
 
# 반복
d = a * 3
print(d)   # [1, 2, 1, 2, 1, 2]
print()
mylist = "This is a book That is a pencil".split()
print(mylist)
i = mylist.index('book')  # i = 3
n = mylist.count('is')    # n = 2
print(i, n)
print()
#[표현식 for 요소 in 컬렉션 [if 조건식]]
list = [n ** 2 for n in range(10) if n % 3 == 0] #0 3 6 9
 
print(list)   # 출력: [0, 9, 36, 81]
print()


print()

