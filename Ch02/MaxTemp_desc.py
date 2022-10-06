import csv                      # CSV 모듈 불러오기

f = open('seoul_desc.csv')           # seoul.csv 파일 읽기 모드로 불러오기
data = csv.reader(f)
header = next(data)             # 맨 윗줄을 header 변수에 저장하기
max_temp = -999                 # 최고 기온을 저장할 변수 초기화
max_date = ''                   # 최고 기온이었던 날짜를 저장할 변수 초기화


# data[0][-1] = float(data[0][-1])
# max_date = data[0][0]
# max_temp = data[0][-1]

data[-1] = float(data[-1])
max_date = data[0]
max_temp = data[-1]


f.close()                       # 파일 닫기
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은', max_date+'로, ', max_temp, '도 였습니다.')      # 출력