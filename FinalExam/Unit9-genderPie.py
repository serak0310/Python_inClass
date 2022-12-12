# 제주도의 성별 인구 비율 파이 차트로 표현하기

import csv
f = open('gender.csv')
data = csv.reader(f)

size = []

name = input('원하시는 지역을 입력해주세요: ')

for row in data:
    if name in row[0]:
        m = 0
        f = 0
        for i in range(101):
            m += int(row[i+3])
            f += int(row[i+106])
        break
size.append(m)
size.append(f)

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.axis("equal")
plt.pie(size, labels=['남성', '여성'], colors=['darkmagenta', 'pink'], autopct='%.1f%%', startangle=90)
plt.legend()
plt.show()