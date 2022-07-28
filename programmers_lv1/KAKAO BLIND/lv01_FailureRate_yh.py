# PROGRAMMERS Lv1 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 작성자 : 조예현
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-07-28

def solution(N, stages):
    answer = []
    clear = {}

    for i in range(1, N+1) :        # Make a Dictionary for calculating of failure rate
      clear[i] = 0

    for i in range(1, N+1) :
      clearNum = 0
      Notclear = 0
      for j in stages :
        if i <= j :
          clearNum += 1            # clearNum is the number of players reached of stage
        if i == j :
          Notclear += 1            # Notclear is the number of players reached of stage, but not clear yet

      if clearNum == 0 :           # if clearNum is 0, the fauilure rate is 0 too
        FauilureRate = 0
      else :   
        FauilureRate = Notclear / clearNum

      clear[i] = FauilureRate
    # this is the function sort in descending order
    clear = sorted(clear.items(), key = lambda item: item[1], reverse = True)

    for i in clear :
      answer.append(i[0])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4, 4, 4, 4, 4]
solution(N, stages)