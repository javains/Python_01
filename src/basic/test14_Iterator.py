# Iterator

# 리스트 Iterable
for n in [1,2,3,4,5]:
    print(n)
 
# 문자열 Iterable
for c in "Hello World":
    print(c)

  # 버전에 관계없이 사용할 수 있는 방식으로 내장 함수 "next(iterator객체)
class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))
 
    def __iter__(self):
        self.index = 0
        return self
 
    def __next__(self):
        if self.index >= self.size:
            raise StopIteration
 
        n = self.data[self.index]
        self.index += 1
        return n
     
 
coll = MyCollection()
for x in coll:
    print(x)


print('*'*50)    


# 2. Generator
#Generator는 Iterator의 특수한 한 형태이다.
#Generator 함수(Generator function)는 함수 안에 yield 를 사용하여 데이타를 하나씩 리턴하는 함수이다.   

# Generator 함수
def gen():
    yield 1
    yield 2
    yield 3
 
# Generator 객체
g = gen()
print(type(g))  # <class 'generator'>
 
# next() 함수 사용
n = next(g); print(n)  # 1
n = next(g); print(n)  # 2
n = next(g); print(n)  # 3
print('*'*50)    

# for 루프 사용 가능
for x in gen():
    print(x)

# Generator는 데이타가 무제한이어서 모든 데이타를 리턴할 수 없는 경우나, 데이타가 대량이어서 일부씩 처리하는 것이 필요한 경우, 혹은 모든 데이타를 미리 계산하면 속도가 느려서 그때 그때 On Demand로 처리하는 것이 좋은 경우 등에 종종 사용된다.
print('*'*50)    

# Generator Expression
g = (n*n for n in range(1001))
 
# g는 generator 객체
print(type(g))  # <class 'generator'>
 
# 리스트로 일괄 변환시
# mylist = list(g)
 
# 10개 출력
for i in range(10):
    value = next(g)
    print(value)
 
# 나머지 모두 출력 
for x in g:
    print(x)