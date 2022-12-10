# Unit07. 우리 동네 인구 구조 시각화하기
# 지역명을 입력받아서 연령별 인구수 데이터 시각화하기

import csv

f = open('age.csv')
data = csv.reader(f)
result = []                             # 결과를 저장할 리스트

name = input('인구 구조가 알고싶은 지역이 이름을 입력해주세요 : ')

for row in data:
    if name in row[0]:                  # 알고싶은 지역의 행정구역이라면
        for i in row[3:]:               # 0세부터 끝(100세 이상)까지 모든 데이터에 반복
            result.append(int(i))       # 정수로 형변환 해 리스트에 저장

# 시각화하기
import matplotlib.pyplot as plt

plt.style.use('ggplot')                 # 격자형으로 그리기
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역의 인구구조')
plt.plot(result)
plt.show()

