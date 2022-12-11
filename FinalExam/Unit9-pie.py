# 혈액형 비율 파이 차트로 표현하기

import matplotlib.pyplot as plt

size = [2441, 2312, 1031, 1233]
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
label = ['A', 'B', 'O', 'AB']

plt.axis('equal')
plt.pie(size, labels=label, colors=color, autopct='%.1f%%', explode=(0,0,0.1,0))
plt.legend()
plt.show()