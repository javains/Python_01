#ctrl+alt+down  라인복사
#ctrl+shift+k   라이삭제
#Data type
print(int(3.9))
print(float(9.9))
print(bool('True')) 
print(bool(0))      #//False
print(bool(''))     #//False
print(bool(' '))    #//True
print('*'*50)

print(5%2)
print(5//2)
a=5;
a = a* 2
a -= 1
print(a)
if a<=10:
    print("=====>",a)


x=10>10
y=10==10
if y:
    print("y : ",y)

if x | y:
    print('x : ',x)      
    print("y : ",y)

a = [1,2,3,4,5]
b=3 in a
print(b)

a="ABC"
b=a
print(a,'  ',b)
print(a is b)
print('*'*50)

p="이름:%s 나이 :%d" %('홍길동',22)
print(p)
import math
p='X=%0.3f,Y=%10.2f' %(math.pi,math.pi)
print(p)

s=','.join(['홍길동','박길동','김유신'])
print(s)
s=''.join(['홍길동','박길동','김유신'])
print(s)

items = '홍길동,박길동,김유신'.split(',')
print(type(items))
print(items)

# 위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)  #출력: Name: 강정수, Age: 30
 
# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s) #출력: Name: 강정수, Age: 30
 
# object의 인덱스 혹은 키를 사용하여 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s) #출력: width: 10, height: 20
