# 에러값이 0이되면=최소가 되면 다시 에러값을 키워줘서 검사를 이어나가야지 업데이트가 가능함
# 태어난 날의 최고기온과 같은 날을 출력
# if row[-1] != '':         결측치 처리. 공백이 아니면 읽어오기

import csv                                              # CSV 모듈 불러오기
birth_temp = 0.0                                        # 생일 온도
trial_dates = []                                        # 비슷한 기온이었던 날짜를 저장할 변수 초기화

#------------------------생일날 최고기온 찾기------------------------
f = open('seoul.csv')                                   # seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data)                                     # 맨 윗줄을 header 변수에 저장하기

for row in data:
    # 만약 데이터가 누락되지 않았다면
    if row[-1] != '':                                     
        row[-1] = float(row[-1])                        # 문자열로 저장된 최고 기온 값을 실수로 변환
        if row[0] == '1999-03-10':
          birth_temp = row[-1]
     
f.close()                                               # 파일 닫기

#------------------------같은 기온의 날짜 찾기------------------------
f = open('seoul.csv')                                   # seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data)                                     # 맨 윗줄을 header 변수에 저장하기

for row in data :
    # 만약 데이터가 누락되지 않았다면
    if row[-1] != '':                                       
        row[-1] = float(row[-1])                        # 문자열로 저장된 최고 기온 값을 실수로 변환
        errorRange = abs(birth_temp-row[-1])            # 오차값 계산
        if errorRange == 0 :                            # 오차값이 0이라면 날짜와 온도 저장
            trial_dates.append(row[0])
   
f.close()                                               # 파일 닫기

#------------------------출력------------------------
print('내 생일날의 최고기온은 ', birth_temp, '도 입니다.')
print('생일 기온과 같은 날은', end=' ')
for i in trial_dates:
    print(i, end=', ')                                  # 출력
print('입니다.')