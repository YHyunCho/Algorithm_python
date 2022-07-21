# PROGRAMMERS Lv1 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 작성자 : 조예현
# 최초 작성일 : 2022-07-15
# 최종 작성일 : 2022-07-21

def solution(a, b) :
  answer = ''
  month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

  date = (sum(month[:a]) + b) % 7

  answer = day[date]

  return answer

a = 5
b = 24
solution(a, b)