# 작년 내 생일의 최고온도와 제일 근사치의 최고 온도
# 작년 내 생일 최고온도 = 17.1도

import csv                      # CSV 모듈 불러오기

f = open('seoul.csv')           # seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data)             # 맨 윗줄을 header 변수에 저장하기
birth_temp = 17.1               # 생일 온도
trial_temp = []                 # 비슷한 기온을 저장할 변수 초기화
trial_date = []                 # 비슷한 기온이었던 날짜를 저장할 변수 초기화
trial_count = 0

for row in data :
    # 만약 데이터가 누락되었다면 최고 기온을 -999로 저장
    if row[-1] == '':
        row[-1] = -999
    # 문자열로 저장된 최고 기온 값을 실수로 변환
    row[-1] = float(row[-1])
    # 만약 지금까지 최고 기온보다 더 높다면 업데이트
    if birth_temp == row[-1] :
        trial_date.append(row[0])
        trial_temp.append(row[-1])
        trial_count = trial_count+1


f.close()                       # 파일 닫기

for i in trial_date:
    print('생일의 기온과 같은 날은', i+'로 ', '도 였습니다.')      # 출력
