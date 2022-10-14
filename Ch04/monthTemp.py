import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
result =[]
next(data)

for row in data:
    if row[0].split('-')[1] == '08':
        result.append(float(row[-1]))

plt.plot(result, 'hotpink')
plt.show()