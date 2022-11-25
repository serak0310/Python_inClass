# 모든 지하철역의 시간대별 승하차 인원 추이 표현하기

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
s_in = [0]*24
s_out = [0]*24

for row in data : 
    row[4:] = map(int, row[4:])
    for i in range(24):
        s_in[i] += row[4 +i*2]
        s_out[i] += row[5+i*2]

import matplotlib.pyplot as plt
#plt.figure(dpi=300)
plt.rc('font', family = "Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()