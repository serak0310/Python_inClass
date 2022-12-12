# 유임 승차 인원이 가장 많은 역 찾기

import csv
f = open('subwayfee.csv', encoding='UTF8')
data = csv.reader(f)
next(data)

label = ['유임승차', '유임하차', '무임승차', '무임하차']
mx = [0] *4
station = ['']*4

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
        if row[i]>mx[i-4]:
            mx[i-4] = row[i]
            station[i-4] = row[3]

for i in range(4):
    print(label[i], station[i])