# PROGRAMMERS Lv1 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

# 작성자 : 조예현
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-07-28

from itertools import *

def solution(nums):
    answer = 0

    Numbers = list(combinations(nums, 3))

    for i in Numbers :
      SumNumbers = sum(i)
      cnt = 0
      
      for j in range(1, SumNumbers+1) :
        if SumNumbers % j == 0 :
          cnt += 1

      if cnt == 2 :
        answer += 1

    return answer

nums = [1, 2, 3, 4]
# nums = [1, 2, 7, 6, 4]
solution(nums)