import matplotlib.pyplot as plt
plt.title('color')          # 제목 설정

# 그래프 그리기
plt.plot([10,20,30,40], color='skyblue', label='skyblue')
plt.plot([40,30,20,10], 'pink', label='pink')
plt.legend()                # 범례 표시
plt.show()


