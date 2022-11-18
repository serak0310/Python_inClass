# 유무임 승하차 인원이 가장 많은 역 찾기

import csv
f = open('subwayfee.csv', encoding='UTF8')
data = csv.reader(f)
next(data)

mx = [0]*4
mx_station = ['']*4
label = ['유임승차', '유임하차', '무임승차', '무임하차']
for row in data :
    for i in range(4,8):
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] +' '+row[1]

for i in range(4):
    print(label[i]+' : '+mx_station[i], mx[i])