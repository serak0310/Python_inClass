# 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기

import csv
import numpy as np
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)

name = input('궁금한 지역의 이름을 입력해주세요:')
result = 0
result_name = ''
mn = 1

for row in data:
    if name in row[0]:
        home = np.array(row[3:], dtype=int)/int(row[2])

for row in data:
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home-away)**2)
    if s < mn and name not in row[0]:
        mn = s
        result = away
        result_name = row[0]

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()



