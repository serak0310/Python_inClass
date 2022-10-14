a = 123
a = 12.34
a = 1+ 2j


print(a.real)             # 실수


print(a.imag)              # 허수


print(a.conjugate)         # 복소수 부호 바꾸기


abs(a)              # 복소수의 크기
print(a)

a = 0o12            # 8진수
print(a)

a = [1, 2, 3, 4]
a[1:3]=['a','b','c']
print(a)

import pandas as pd
data2 = [10, 20, 30, 40, 50]
data3 = ["1반", "2반", "3반", "4반", "5반"]

sr5 = pd.Series(data3, index=data2)
print(sr5)