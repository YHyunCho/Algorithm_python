# PROGRAMMERS Lv1 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 작성자 : 조예현
# 최초 작성일 : 2022-07-15
# 최종 작성일 : 2022-07-15

def solution(a, b) :
  answer = ''
  date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  day = ['0', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

  day_cul = int(b / 7) * 7
  b -= day_cul

  print(day[b])
  

a = 5
b = 24
solution(a, b)