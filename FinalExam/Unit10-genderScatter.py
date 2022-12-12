import csv
import math

f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
size = []

name = input('궁금한 동네를 입력해주세요: ')

for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i])+int(row[i+103])))
        break

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.scatter(m, f, s=size, c=range(101), alpha=0.5, cmap='jet')
plt.plot(range(max(m)), range(max(m)), 'g')
plt.colorbar()
plt.show()