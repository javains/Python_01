# numpy 패키지
# numpy는 과학 계산을 위한 라이브러리로서 다차원 배열을 처리하는데 필요한 여러 유용한 기능을 제공
# numpy 설치     pip install numpy 
# G:\2019\python\python_work\Python_01\src\util_lib> pip install numpy
# Requirement already satisfied: numpy in c:\users\user\appdata\local\programs\python\python36-32\lib\site-packages (1.14.2)

# numpy 배열은 동일한 타입, 배열의 차원을 rank 
# 2행 3열 2차원 배열에서 rank는 2 이고, shape는 (2, 3) 
import numpy as np

list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a.shape) # (4, ) 튜플에 하나의 요소만 있으면 문법상 콤마를 뒤에 붙인다
print(a) 
print()
b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # (2, 3)
print(b[0,0])  # 1  
print(b) 
print('*'*50)
import numpy as np
 
a = np.zeros((2,2))
print(a)
# 출력:
# [[ 0.  0.]
#  [ 0.  0.]]
 
a = np.ones((2,3))
print(a)
# 출력:
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]
 
a = np.full((2,3), 5)
print(a)
# 출력:
# [[5 5 5]
#  [5 5 5]]
 
a = np.eye(3)
print(a)
# 출력:
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
 
a = np.array(range(20)).reshape((4,5))
print(a)
# 출력:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]
print('*'*50)
# numpy 슬라이싱
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
 
# 슬라이스
a = arr[0:2, 0:2]
print(a)
# 출력:
# [[1 2]
#  [4 5]]
 
a = arr[1:, 1:]
print(a)
# 출력:
# [[5 6]
#  [8 9]]

# 정수 인덱싱
s = arr[[0, 2], [1, 2]]
print(s) # 2,9
print()

# numpy 부울린 인덱싱 (boolean indexing)
import numpy as np
 
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
 
# 배열 a 에 대해 짝수면 True, 홀수면 False 
bool_indexing = (a % 2 == 0)
 
print(bool_indexing)
# 출력: 부울린 인덱싱 배열
# [[False  True False]
#  [ True False  True]
#  [False  True False]]
 
# 부울린 인덱스를 사용하여 True인 요소만 뽑아냄
print(a[bool_indexing])
# 출력:
# [2 4 6 8]
 
# 더 간단한 표현
n = a[ a % 2 == 0 ]
print(n)