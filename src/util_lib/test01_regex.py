# 정규 표현식 (Regular Expression)
# Regex를 위한 모듈인 re 모듈을 사용한다.

import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
# re 모듈의 compile 함수는 정규식 패턴을 입력으로 받아들여 정규식 객체를 리턴
regex = re.compile("에러 1033")    #re.RegexObject 클래스 객체 리턴
# search() 는 처음 매칭되는 문자열만 리턴하는데, 매칭되는 모든 경우를 리턴하려면 findall() 을 사용
mo = regex.search(text)   #MatchObject 객체를 리턴
if mo != None:
    print(mo.group()) # MatchObject 객체로부터 실제 결과 문자열을 얻기 위해서는 group() 메서드를 사용

regex = re.compile("에러\s\d+")
mc = regex.findall(text)
print(mc)


# 전화번호 
text = "문의사항이 있으면 010-7221-2345 으로 연락주시기 바랍니다."
 
regex = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)    

regex = re.compile('\d{3}-\d{4}-\d{4}')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber) 
