# Thread
# 파이썬은 실제 다중 CPU 환경에서 동시에 여러 파이썬 코드를 병렬로 실행할 수 없으며 인터리빙(Interleaving) 방식으로 코드를 분할하여 실행한다. 
# 다중 CPU 에서 병렬 실행을 위해서는 다중 프로세스를 이용하는 multiprocessing 모듈을 사용한다.

import threading, requests, time

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread  sum", total)
 
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print('getHtml',url, len(resp.text), ' chars')

 
class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) 
        self.url = url
 
    def run(self):
        resp = requests.get(self.url)
        time.sleep(5)
        print('HtmlGetter',self.url, len(resp.text), ' chars')

tc = HtmlGetter('http://google.com')
tc.daemon=True
tc.start()
 
t = threading.Thread(target=sum, args=(1, 1000000))

t.start()

t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()

print("###    End ###")