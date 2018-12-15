# 예외처리

# try:
#   문장1
#   문장2
# except:
#   예외처리
# finally:
#   마지막에 항상 수행

def calc0(values):
     sum = values[0] + values[1] + values[2]
     print(sum)


def calc(values):
    sum = None
    # try...except...else
    try:
       sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print('인덱스에러')
    except Exception as err:
        print(str(err))
    else:
        print('에러없음')
    finally:
        print(sum)
 
# 테스트
calc([1, 2, 3, 6]) # 출력: 에러없음 6
calc([1, 2])       # 출력: 인덱스에러 None
calc([1, 'aaaa',3])       # 출력: 인덱스에러 None

def calc3(values):
    sum = None
    try:
       sum = values[0] + values[1] + values[2]
    except (IndexError, ValueError):
        print('오류발생')
    print(sum)


print('=========  calc End  ============')

# 파일 에러 처리 예제
try:
   fp = open("test.txt", "r")
   try:
      lines = fp.readlines()
      print(lines)
   finally:
      fp.close()
except IOError:
   print('파일에러')



print('=========  file read  End  ============')

# with 문을 써서 해당 블럭이 끝나면 자동으로 파일을 닫는 코드의 예
with open('test.txt', 'r') as fp:
    lines = fp.readlines()
    print(lines)

print('=========   End  ============')
