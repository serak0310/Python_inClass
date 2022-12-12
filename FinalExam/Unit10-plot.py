# 성별 연령별 인구 데이터 꺾은선 그래프로 표현하기

import csv 
f= open('gender.csv')
data = csv.reader(f)

m = []
f = []
name = input('궁금한 동네를 입력해주세요: ')

for row in data:
    if name in row[0]:
        for i in range(3, 104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break

import matplotlib.pyplot as plt

plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()