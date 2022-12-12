# 찾고 싶은 지역 이름 입력해서 항아리 모양 그래프 그리기

import csv
f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('궁금한 지역의 이름을 입력해주세요: ')

# for문 두 번 도는 방식
# for row in data:
#     if name in row[0]:
#         for i in row[3:104]:
#             m.append(-int(i))
#         for i in row[106:]:
#             f.append(int(i))

# # for문 한 번 도는 방식
# for row in data:
#     if name in row[0]:
#         for i in range(101):
#             m.append(-int(row[i+3]))
#             f.append(int(row[-(i+1)]))
# f.reverse()

for row in data:
    if name in row[0]:
        for i in range(101):
            m.append(-int(row[i+3]))
            f.append(int(row[i+106]))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.title(name+' 지역의 인구 성별 어쩌구')
plt.legend()
plt.show()