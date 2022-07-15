# PROGRAMMERS Lv1 수박수박수박수박수박수?
# https://school.programmers.co.kr/learn/courses/30/lessons/12922

# 작성자 : 조예현
# 최초 작성일 : 2022-07-15
# 최종 작성일 : 2022-07-15

def solution(n) :
  answer = ''
  watermelon = '수박'

  len_watermelon = int(n / 2)

  for i in range(len_watermelon) :
    answer += watermelon

  if n % 2 == 1 :
    answer += '수'

  return answer

n = 3
n = 4
solution(n)