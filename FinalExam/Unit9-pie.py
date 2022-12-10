# 혈액형 비율 파이 차트로 표현하기

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

scale = [2441, 2312, 1031, 1233]
label = ['A', 'B', 'O', 'AN']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']

plt.axis('equal')
plt.pie(scale, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.1,0))
plt.legend()
plt.show()