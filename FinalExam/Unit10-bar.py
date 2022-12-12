# 연령별 남성인구-여성인구 값 막대 그래프로 표현하기

import csv 
f= open('gender.csv')
data = csv.reader(f)

result = []
name = input('궁금한 동네를 입력해주세요: ')

for row in data:
    if name in row[0]:
        for i in range(3, 104):
            result.append(int(row[i])-int(row[i+103]))
        break

import matplotlib.pyplot as plt

plt.bar(range(101), result)
plt.show()