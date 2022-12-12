# 유임 승차 비율이 가장 높은 역 찾기

import csv

f = open('subwayfee.csv',  encoding='UTF8')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
station = ''

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    if (row[6] != 0) and ((row[4]+row[6])>100000):
        rate = row[4] / (row[4]+row[6])
        if rate > mx:
            mx = rate
            station = row[3] + ' ' + row[1]

print(station, round(mx*100, 2))
