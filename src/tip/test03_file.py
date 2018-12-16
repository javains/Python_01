# 텍스트 파일
# 파일을 오픈하고, 데이타를 읽거나 쓴 후, 파일을 close()
# read(), readline(), readlines() 
# write(), writelines()
# Python은 Universal Newline 이라고 하여 플랫폼에 상관없이 라인 Delimeter로 "\n"을 사용
# 실행 플랫폼이 윈도우즈의 경우 이 Universal Newline은 CRLF (\r\n) 으로 변경되고, 맥이나 리눅스에서는 LF (\n)로 자동으로 사용된다.

f = open('../data/test.txt', mode='wt', encoding='utf-8')
f.write("Hello, World\n");
f.write("안녕하세요?")
f.close()

f = open('../data/test.txt', mode='rt', encoding='utf-8')
s1 = f.readline()  # Hello, World\n
s2 = f.readline()  # 안녕하세요?
print(s1)
print(s2)
f.close()
#########################################
print()
import sys
f = open('../data/test.txt', mode='rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line)
f.close()
#######################################
print('')
try:
    f = open('../data/test.txt', mode='rt', encoding='utf-8')
    for line in f:
        print(line)
finally:
    f.close()
#########################################
print('')

with open('../data/test.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        print(line)


