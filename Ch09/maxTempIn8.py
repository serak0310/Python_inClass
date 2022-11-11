import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
aug = []

for row in data:
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month == '08':
            aug.append(float(row[-1]))

plt.hist(aug, bins=100, color='r')
plt.show()
