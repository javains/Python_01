# pandas  =>   pip install pandas 
# pandas는 데이타 분석(Data Analysis)을 위해 널리 사용되는 파이썬 라이브러리 패키지이다.
# pandas는 과학용 파이썬 배포판인 아나콘다(Anaconda)에 기본적으로 제공

import pandas as pd

# Series 배열/리스트와 같은 일련의 시퀀스 데이타를 받아들이는 1차원 자료구조
data = [1, 3, 5, 7, 9]
s = pd.Series(data)
print(s)
print()
# DataFrame : 2차원 자료구조인  행과 열이 있는 테이블 데이타(Tabular Data)
data = {
    'year': [2014,2015,2016, 2017, 2018],
    'rate': [2.4,2.5,2.8, 3.1, 3.0],
    'GDP': ['1.537M','1.60M','1.637M', '1.73M', '1.83M']
}
 
df = pd.DataFrame(data)
print(df)
print()
# 데이타 엑세스
print(df['year'])
print()
print(df['year']>2016)
print('----------------------------------')
print(df[df['year']>2016])
print('----------------------------------')
#sum = df.sum()
sum = df['rate'].sum()
avg=df['rate'].mean()
print('---  sum  avg----')
print(sum,',',avg)
print('----------------------------------')
print(df.describe())
print('----------------------------------')
# Panel  3차원 자료구조인 Panel은 Axis 0 (items), Axis 1 (major_axis), Axis 2 (minor_axis) 등 3개의 축
# numpy를 사용하여 3차원 난수를 발생시킨 후, 이를 pandas.Panel() 에 적용




