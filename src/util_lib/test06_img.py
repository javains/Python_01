# 파이썬에서의 이미지 처리 , 이미지 파일 읽고 쓰기
# pip install Pillow
# Pillow는 파이썬 이미징 라이브러리로서 여러 이미지 파일 포맷을 지원
# 이미지 크기를 변형하거나 회전 및 Transform, 그리고 필터링 등 다양한 이미지 프로세싱 작업들을 할 수 있다.

from PIL import Image
# 이미지 열기
im = Image.open('../data/python.png')
 
# 이미지 크기 출력
print(im.size)
# Thumbnail 이미지 생성
size = (64, 64)
im.thumbnail(size)  

# 이미지 JPG로 저장
im.save('../data/python.jpg')




print('END')
