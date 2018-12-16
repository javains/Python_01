# -*- coding:utf-8 -*-
 
import smtplib
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP('smtp.server', 587)
smtp.ehlo()      # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('id', 'pw')
 
msg = MIMEText('본문 테스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = 'javains@naver.com'
smtp.sendmail('~~', 'javains@naver.com', msg.as_string())
 
smtp.quit()
print('email send ok...')