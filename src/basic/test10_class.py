#클래스
#메서드(method), 속성(property), 클래스 변수(class variable), 인스턴스 변수(instance variable), 초기자(initializer), 소멸자(destructor) 등

class MyClass:
    pass


# attribute를 동적으로 추가할 수 있고, 메서드도 일종의 메서드 객체로 취급하여 attribute에 포함한다
# 인스턴스 메서드(instance method), 정적 메서드(static method), 클래스 메서드(class method)

class Rectangle:
    count = 0  # 클래스 변수
 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
 
    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
 
    def print(self):
        print('width:%d,height:%d,area:%.2f'%(self.width,self.height,self.calcArea()))
    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight   
 
    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)  

    def __add__(self, other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj     
 

# 클래스 변수    Rectangle.count
# 인스턴스 변수  self.width 과 같이 "self." 을 사용하여 엑세스
# Initializer (초기자)   __init__()   두개의 밑줄 (__)


# 테스트

# 객체 생성
r = Rectangle(2, 3)
r.print() 
# 메서드 호출
area = r.calcArea()
# print("area = ", area)
 
# 인스턴스 변수 엑세스
r.width = 10
# print("width = ", r.width)
r.print() 
# 클래스 변수 엑세스
print(Rectangle.count)
# print(r.count)
print()

square = Rectangle.isSquare(5, 5)        
# print(square)   # True        
 
rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()        # 2 
Rectangle.printCount()  
print(rect1.calcArea())
print(rect2.calcArea())

# 소멸자(__del__) 메서드, 두 개의 객체를 ( + 기호로) 더하는 __add__ 메서드, 
# 두 개의 객체를 ( - 기호로) 빼는 __sub__ 메서드, 두 개의 객체를 비교하는 __cmp__ 메서드, 문자열로 객체를 표현할 때 사용하는 __str__ 메서드 등

rect3= rect1 + rect2  # __add__()가 호출됨
print(rect3.calcArea())

# 클래스 상속과 다형성   Multiple Inheritance


class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
 
class Dog (Animal):
    def speak(self):
        print("bark")
 
class Duck (Animal):
    def speak(self):
        print("quack")

dog = Dog("doggy") # 부모클래스의 생성자
print(dog.name) # 부모클래스의 인스턴스변수
dog.move()   # 부모클래스의 메서드
dog.speak()  # 파생클래스의 멤버

animals = [Dog('doggy'), Duck('duck')]
 
for a in animals:
    a.speak()
