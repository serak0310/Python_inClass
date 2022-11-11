import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

birthYear = int(input("자신의 생일의 '년'을 입력해주세요."))
birthMonth = int(input("자신의 생일의 '월'을 입력해주세요."))

daysOfLeapyear = [31,29,31,30,31,30, 31,31,30, 31, 30, 31]
daysOfNotLeapyear = [31,28,31,30,31,30, 31,31,30, 31, 30, 31]

if (birthYear % 4 == 0 and birthYear % 100 != 0) or birthYear % 400 == 0:   # (4년으로 나누어 떨어지고, 100으로 나누어 떨어지지 않는 경우) 또는 400으로 나누어 떨어지는 경우는 윤년이다.
	# leap year
    daysOfMonth = daysOfLeapyear[birthMonth-1]
else:
    # not leap year
    daysOfMonth = daysOfNotLeapyear[birthMonth-1]

day = [[] for i in range(daysOfMonth)]

for row in data:
    if row[-1] != "":
        if int(row[0].split('-')[1]) == birthMonth:
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.style.use('ggplot')
# plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()