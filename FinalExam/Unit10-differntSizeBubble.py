# 위치, 크기가 서로 다른 100개의 점 만들기

import matplotlib.pyplot as plt
import random

x = []
y = []
size = []

for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()