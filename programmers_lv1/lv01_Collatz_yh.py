# PROGRAMMAERS LV01 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943

# 작성자 : 조예현
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-22

def solution(num):
    answer = 0

    while num != 1 :
      if num % 2 == 0 :
        num /= 2
        answer += 1
      else :
        num = num * 3 + 1
        answer += 1

      if answer == 500 :
        answer = -1
        break

    return answer

n = 626331
solution(n)