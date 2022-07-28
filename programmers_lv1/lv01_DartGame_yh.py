# PROGRAMMERS Lv1 [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 작성자 : 조예현
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-07-28

def solution(dartResult):
    answer = 0
    dartList = {1: [0, '', ''], 2: [0, '', ''], 3: [0, '', '']}
    number = []

    L = dartResult.find('10')
    if L == 0 :
        dartList[1][0] = 10
        dartResult = dartResult.replace('10', '--')
    elif L > 0 and L < 4 :
        dartList[2][0] = 10
        dartResult = dartResult.replace('10', '--')
    elif L > 3 :
        dartList[3][0] = 10
        dartResult = dartResult.replace('10', '--')

    for i in range(1, 4) :
        for j in range(len(dartResult)) :
            if (ord(dartResult[j]) >= 48 and ord(dartResult[j]) <= 57) :
                if dartList[i][0] == 0 :
                    dartList[i][0] = int(dartResult[j])
                    dartResult = dartResult.replace(dartResult[j], '-')
            continue
    print(dartResult)
    dartResult = dartResult.split('-') 

    print(dartResult)

    for i in range(1, 4) :
        dartList[i][1] = dartResult[i]

    print(dartList) 


          
    return answer

dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
# dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
solution(dartResult)