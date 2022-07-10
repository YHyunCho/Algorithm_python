# PROGRAMMAERS LV01 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

# 작성자 : 조예현
# 최초 작성일 : 2022-07-10
# 최종 작성일 : 2022-07-10

def solution(x):
    answer = True
    # [int(a) for a in str(x)] is the function seperates integer number
    harshad = [int(a) for a in str(x)]
    # 'sum' add all the numbers in list of 'harshad'
    sum_harshad = sum(harshad)

    if x % sum_harshad != 0 :
      answer = False

    return answer

#arr = 10
arr = 11

solution(arr)