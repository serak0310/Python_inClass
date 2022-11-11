import csv
f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data:
    if name in row[0]:
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))
        break                   # 첫번째 데이터만 저장하고 반복문 빠져나가기

print(len(m), len(f))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = "Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()