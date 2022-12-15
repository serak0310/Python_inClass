# 모든 지하철역의 시간대별 승하차 인원 추이 표현하기

import csv
f = open('subwaytime.csv')
data = csv.reader(f)

s_in = [0] *24
s_out = [0]*24

next(data)
next(data)

for row in data:
    row[4:] = map(int, row[4:])
    for i in range(24):
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.xticks(range(24), range(4,28))
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.legend()
plt.show()