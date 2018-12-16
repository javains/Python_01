# numpy 패키지
# numpy는 과학 계산을 위한 라이브러리로서 다차원 배열을 처리하는데 필요한 여러 유용한 기능을 제공
# numpy 연산

import numpy as np
 
a = np.array([1,2,3])
b = np.array([4,5,6])
 
# 각 요소 더하기
c = a + b
# c = np.add(a, b)
print(c)  # [5 7 9]
 
# 각 요소 빼기
c = a - b
# c = np.subtract(a, b)
print(c)  # [-3 -3 -3]
 
# 각 요소 곱하기
# c = a * b
c = np.multiply(a, b)
print(c)  # [4 10 18]
 
# 각 요소 나누기
# c = a / b
c = np.divide(a, b)
print(c)  # [0.25 0.4 0.5]

print()
# numpy에서 vector와 matrix의 product를 구하기 위해서 dot() 함수를 사용한다. 
import numpy as np
 
lst1 = [
    [1,2],
    [3,4]
]
 
lst2 = [
    [5,6],
    [7,8]
]
a = np.array(lst1)
b = np.array(lst2)
 
c = np.dot(a, b)
print(c)
# 출력:
# [[19 22]
#  [43 50]]    

print()
# 각 배열 요소들을 더하는 sum() 함수,  곱하는 prod() 함수 등을 사용할 수 있다.
# 선택옵션으로 axis 을 지정할 수 있는데, 
# sum()에서 axis가 1 이면 행끼리 더하는 것이고, axis가 0 이면 열끼리 더하는 것이다
import numpy as np
 
a = np.array([[1,2],[3,4]])
print(a) 
s = np.sum(a)
print(s)   # 10
 
# axis=0 이면, 컬럼끼리 더함
# axis=1 이면, 행끼리 더함
s = np.sum(a, axis=0)
print(s)   # [4 6]
 
s = np.sum(a, axis=1)
print(s)   # [3 7]
 
s = np.prod(a)
print(s)   # 24