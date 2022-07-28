# PROGRAMMERS Lv1 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501

# 작성자 : 조예현
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-07-28

def solution(absolutes, signs):

    for i in range(len(signs)) :
      if signs[i] == False :
        absolutes[i] = -(absolutes[i])
    
    return sum(absolutes)

# absolutes = [4, 7, 12]
# signs = [True, False, True]
absolutes = [1, 2, 3]
signs = [False, False, True]
solution(absolutes, signs)