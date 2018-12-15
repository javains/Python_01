#if while for
x=9
if x < 10:
    print(x)
    print("한자리수")

if x < 10:
    pass
else:
    print(x)   

x = 10
if x < 10:
    print("한자리수")
elif x < 100:
    print("두자리수")
else:
    print("세자리 이상")

print('*'*50)

i=1
while i <= 5:
    print(i)
    i += 1
print('*'*50)
sum = 0
for i in range(11):
    sum += i
print(sum)
list = ["This", "is", "a", "book"]
for s in list:
    print(s)
print('*'*50)

numbers = range(2, 11, 2)
 
for x in numbers:
    print(x)
print('*'*50)

for i in range(10):
    print(i," Hello")        