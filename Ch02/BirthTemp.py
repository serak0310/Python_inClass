
# # 작년 내 생일의 최고온도와 제일 근사치의 최고 온도
# # 작년 내 생일 최고온도 = 17.1도

# import csv                      # CSV 모듈 불러오기

# f = open('seoul.csv')           # seoul.csv 파일 읽기 모드로 불러오기
# data = csv.reader(f)
# header = next(data)             # 맨 윗줄을 header 변수에 저장하기
# birth_temp = 17.1               # 생일 온도
# trial_temps = []                 # 비슷한 기온을 저장할 변수 초기화
# trial_date = []                 # 비슷한 기온이었던 날짜를 저장할 변수 초기화
# trial_count = 0

# trial_range = 999               # 생일기온 - |추측기온| : 오차값 저장할 변수 초기화
# trial_temp = 0                  # 비슷한 기온 저장할 변수 초기화

# for row in data :
#     # 만약 데이터가 누락되었다면 최고 기온을 -999로 저장
#     if row[-1] == '':
#         row[-1] = -999
#     # 문자열로 저장된 최고 기온 값을 실수로 변환
#     row[-1] = float(row[-1])
#     # 만약 생일과 같은 기온일 때가 있다면
#     if birth_temp == row[-1] :
#         trial_date.append(row[0])
#         trial_temps.append(row[-1])
#         trial_count = trial_count+1

# # 만약 생일과 같은 기온일 때가 없었다면
# if len(trial_date) == 0:
#     # 가장 비슷한 기온 찾기
#     for row in data :
#         # 오차값 계산
#         errorRange = birth_temp-abs(row[-1])       
#         # 만약 지금까지 오차값보다 작다면
#         if errorRange <= trial_range :
#             trial_range = errorRange
#             trial_temp = row[-1]


    

# f.close()                       # 파일 닫기

# for i in trial_date:
#     print('생일의 기온과 같은 날은', i+'로 ', '도 였습니다.')      # 출력

