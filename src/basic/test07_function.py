#함수
# def 함수명(입력파라미터):
#     문장1
#     문장2
#     [return 리턴값]

def sum(a, b):
    s = a + b
    return s
 
total = sum(4, 7)
print(total)
print()

# 함수내에서 i, mylist 값 변경
def f(i, mylist):
    i = i + 1
    mylist.append(i)
 
k = 10       # k는 int (immutable)
m = [1,2,3]  # m은 리스트 (mutable)
 
f(k, m)      # 함수 호출
print(k, m)  # 호출자 값 체크 , 출력: 10 [1, 2, 3, 0]
print()

# Default Parameter

def calc(i, j, factor = 1):
    return i * j * factor
 
result = calc(10, 20)
print(result)

result = calc(10, 20,30)
print(result)
print()

#Named Parameter
def report(name, age, score):
    print(name, score)
 
report(age=10, name="Kim", score=80)
print()

#가변길이 파라미터
def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot
 
t = total(1,2)
print(t)
t = total(2,4,6,8,9)
print(t)
print()

#리턴값
def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot
 
count, sum = calc(1,5,2,6)  # (count, tot) 튜플을 리턴
print(count, sum)
print()


