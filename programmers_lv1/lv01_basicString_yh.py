# PROGRAMMAERS LV01 문자열 다루기 기본
#https://school.programmers.co.kr/learn/courses/30/lessons/12918

# 작성자 : 조예현
# 최초 작성일 : 2022-07-10
# 최종 작성일 : 2022-07-10

def solution(s) :
  
  answer = True

  if len(s) != 4 and len(s) != 6 :
    answer = False
  else : 
    answer = s.isdigit()

  return answer

#s = "a234"
s = "1234"
solution(s)