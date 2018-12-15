#모듈
#보통 하나의 파이썬 .py 파일이 하나의 모듈이 된다. 
#모듈 안에는 함수, 클래스, 혹은 변수들이 정의될 수 있으며, 실행 코드를 포함할 수도 있다.
#import 모듈1[, 모듈2[,... 모듈N]
#파이썬은 다양한 모듈을 제공 • 
# 문자열(string), 날짜(date), 시간(time), 수학(math), 분수(fraction), 십진법(decimal), 랜덤(random), 파일(file), 
# sqlite3, os, sys, threading, xml, http 등등 약 200개 정도의 다양한 모듈들이 존재

import math
n = math.factorial(5)
print('5! => ',5)

# factorial 함수만 import
from math import factorial  
 
n = factorial(5) / factorial(3) 
print(n)

# from...import... 방식으로 import 된 함수는 호출시 모듈명 없이 직접 함수명 사용
# 여러 함수를 import
from math import (factorial,acos)
n = factorial(3) + acos(1)
 
# 모든 함수를 import
from math import *
n = sqrt(5) + fabs(-12.5) 

#함수명 as Alias
from math import factorial as f
n = f(5) / f(3)
print(n)
print()
# 모듈의 위치
# 현재 디렉토리  , 환경변수 PYTHONPATH에 지정된 경로, Python이 설치된 경로 및 그 밑의 라이브러리 경로
#        ==> 이러한 경로들은 모두 취합되어 시스템 경로인 sys.path에 리스트 형태로 저장

import sys
print(sys.path)
print()
sys.path.append('c:\lib')
print(sys.path)
print('-'*70)

# exec.py
# from mylib import *
#from mylib import *

#import mymodule 
#i = add(10,20)
# i = substract(20,5)


print(__name__)
print(sys.argv[1])  # commandline parameter