import pandas as pd

sr1 = pd.Series(['1반', '2반', '3반', '4반'], index=[1,2,3,4])
print(sr1)

print(sr1[1])