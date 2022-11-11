# 발표할 학생 순서 랜덤으로 정하기
# 중복 없음
import random

totalNum = int(input('발표할 학생 수를 입력해주세요.'))
student = random.sample(range(1,totalNum+1),totalNum) 
print(student)
