# Matplotlib를 이용하여 데이타 시각화(Data Visualization)
# Matplotlib는 파이썬에서 데이타를 차트나 플롯(Plot)으로 그려주는 라이브러리 패키지
# 과학용 파이썬 배포판인 아나콘다(Anaconda)를 설치해서 Jupyter Notebook을 사용하면 시각적.

from matplotlib import pyplot as plt
 
plt.plot([1,2,3,4], [110,100,130,120])
plt.show()

from matplotlib import pyplot as plt
 
plt.plot(["Seoul","Paris","Seattle"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response ')
plt.title('Experiment Result')
plt.show()

from matplotlib import pyplot as plt
 
plt.plot([2014,2015,2016,2017,2018], [55,77,66,59,44])
plt.plot([2014,2015,2016,2017,2018],[66,84,72,77,88])
plt.xlabel('year')
plt.ylabel('.....')
plt.title('.... Result')
plt.legend(['aaaa', 'bbb'])
plt.show()

from matplotlib import pyplot as plt
 
y = [5, 3, 7, 10]
x = range(len(y))
plt.bar(x, y, width=0.7, color="red")
plt.show()

plt.pie(y,colors=['blue','red','gray','black'])
plt.legend(['aaaa', 'bbb','ccc','ddd'])
plt.show()