# CSV  -> Comma-separated values
# import csv    기본 내장 모듈

import csv
 
f = open('../data/titanic.csv', 'r', encoding='utf-8')
read = csv.reader(f)
for line in read:
    print(line)
f.close()    

import csv    
f = open('../data/output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "홍길동", '010-222-3434'])
wr.writerow([2, "이순신", '010-555-0034'])
f.close()

print('=======================================')
f = open('../data/output.csv', 'r', encoding='utf-8')
read = csv.reader(f)
for line in read:
    print(line)
f.close()  