# PROGRAMMERS Lv1 [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 작성자 : 조예현
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-08-18

def solution(dartResult):
    square = {"S":1, "D":2, "T":3}                      # Dictionary that saved the square value
    dartResult = dartResult.replace("10", "N")          # if there're "10" replace to "N"
    stack = []

    for i in dartResult :
        if i.isdigit() or i == "N" :                    # 'isdigit' is function checks whether a string is a number of not
            if i == "N" :
                stack.append(10)
            else :
                stack.append(int(i))
        elif i in ["S", "D", "T"] :
            num = stack.pop()                           # 'pop' is function returns and deletes the last element in list
            stack.append(num ** square[i])
        elif i =="#" :
            stack[-1] *= -1
        elif i =="*" :
            num = stack.pop()
            if len(stack) :
                stack[-1] *= 2
            stack.append(2 * num)

    return sum(stack)

# dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
# dartResult = '1D2S3T*'
solution(dartResult)