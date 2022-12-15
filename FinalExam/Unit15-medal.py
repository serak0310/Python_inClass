# 금메달 기준으로 데이터 정렬하기

import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
summer = df[1].iloc[:, :5]                          # 하계 올림픽에 대한 데이터만 추출하기
summer.columns = ['경기수', '금', '은', '동', '계']  # 칼럼 이름 설정하기
print(summer.sort_values('금', ascending=False))    # 금메달 기준으로 데이터 정렬하기