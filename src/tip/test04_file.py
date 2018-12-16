# 바이너리 파일

with open("../data/python.png", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        print(byte)
        byte = f.read(1)

# 바이너리 쓰기
data = [1, 2, 3, 4, 5]
with open("test.bin", "wb") as f:
    f.write(bytes(data))
 
# 바이너리 읽기
source = open("../data/python.png", "rb") 
target = open("../data/copy.png", "wb") 

while True:
    s = source.read()
    if s == b'':
        break
    target.write(s)


source.close()
target.close()  