# 아침 7시 승차 데이터 막대 그래프로 표현하기

import csv
f = open('subwaytime.csv', encoding='cp949')
data = csv.reader(f)

next(data)
next(data)
result = []

for row in data:
    row[4:] = map(int, row[4:])
    result.append(row[10])

import matplotlib.pyplot as plt
# result.sort()
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()