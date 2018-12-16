# 외부 데이타 읽고 쓰기
# pandas는 CSV 파일, 텍스트 파일, 엑셀 파일, SQL 데이타베이스, HDF5 포맷 등 다양한 외부 리소스에 데이타를 읽고 쓸 수 있는 기능을 제공

import pandas as pd
# pip install xlrd
df = pd.read_excel('../data/Book1.xlsx')
print(df)

from matplotlib import pyplot as plt
y = df['kor']
x = df['name']
plt.bar(x, y, width=0.7, color="blue")
plt.show()


# titanic.csv
tdf = pd.read_csv('../data/titanic.csv')
#print(tdf)
print(tdf[tdf['pclass']=='1st'])