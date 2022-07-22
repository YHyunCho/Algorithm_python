# PROGRAMMERS LV01 가운데 글자 가져오기
# https://school.programmers.co.kr/learn/courses/30/lessons/12903

# 작성자 : 조예현
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-22

def solution(s) :
  answer = ''

  num = int(len(s) / 2)
  
  if len(s) % 2 == 0 :
    answer = s[num-1] + s[num]
  else :
    answer = s[num]

  return answer

s = "abcde"
solution(s)