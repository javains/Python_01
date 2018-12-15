# 1.List Comprehension

#  for 루프를 돌면 특정 조건에 있는 입력데이타를 변형하여 리스트로 출력하는 코드를 간단한 문법으로 표현한 것

# [출력표현식 for 요소 in 입력Sequence [if 조건식]]

oldlist = [1, 2, 'A', 1,3.3,False, 3]
newlist = [i*i for i in oldlist if type(i)==int]
print(newlist)   # 출력: [1, 4, 1, 9]

# 2.Set Comprehension

oldlist = [1,2.2, 1, 2, 3, 3, 4]
newset = {i*i for i in oldlist}
print(newset)  # 출력 : {16, 1, 9, 4,4.84}

# 3.Dictionary Comprehension
id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()}
print(name_id)


# 4. if 조건식 안에 필터링 함수를 사용한 경우
def isodd(val):
    return val % 6 == 0
 
mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict)