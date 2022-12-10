# 막대 그래프를 활용해 우리 동네 인구 구조 시각화하기
# 수직 막대 그래프

import csv

f = open('age.csv')
data = csv.reader(f)

result = []
for row in data:
    if '노형동' in row[0]:
        for i in row[3:]:
            result.append(int(i))

import matplotlib.pyplot as plt
plt.bar(range(101), result)                     # [x축], [y축] 쌍을 이룸
plt.show()