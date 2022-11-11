import csv
f = open('age.csv')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

for row in data:
    if name in row[0]:
        for i in row[3:] :
            # result.append(int(i.replace(',','')))
            result.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = "Malgun Gothic")
plt.title(name+' 지역의 인구 구조')
plt.plot(result)
plt.show()