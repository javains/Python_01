#  pip install requests

import requests
 
resp = requests.get( 'http://daum.net' )
# resp.raise_for_status()
 
if (resp.status_code == requests.codes.ok):
    html = resp.text
    #print(html)

print()
print()
import requests
 
resp = requests.get('http://naver.com/')
resp.raise_for_status()
 
#resp.encoding=None   # None 으로 설정
#resp.encoding='euc-kr'  # 한글 인코딩
 
html = resp.text
print(html)    
print()

# 웹페이지 HTML 문서를 파싱(Parsing)하기 위해서는 BeautifulSoup 라는 모듈을 사용할 수 있다. 
# BeautifulSoup  설치  => pip install beautifulsoup4

import bs4
html = "<html><body><p> hello world </p><p>.....</p></body></html>"
bs = bs4.BeautifulSoup(html, 'html.parser')   # BeautifulSoup 객체를 생성
tags = bs.select('p') 
print(tags)

for tag in tags:
    print(tag,' -> ',tag.getText())

print('*'*50)

import requests, bs4
 
resp = requests.get('https://finance.naver.com/')
resp.raise_for_status()
 
#resp.encoding='euc-kr'
html = resp.text
 
bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('div.header') # Top 뉴스
print(tags)
#title = tags[0].getText()
#print(title)
