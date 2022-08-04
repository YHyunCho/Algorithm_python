# PROGRAMMERS Lv1 [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 작성자 : 조예현
# 최초 작성일 : 2022-07-28
# 최종 작성일 : 2022-08-03

def solution(dartResult):
    answer = 0
    dartList = []
    number = 0

    for i in range(len(dartResult)) :
        if (ord(dartResult[i]) >= 48 and ord(dartResult[i]) <= 57) :
            if dartResult[i+1] == '0' :
                number = int(dartResult[i:i+2])
                dartResult = dartResult.replace(dartResult[i+1], '_')
                continue
            else :
                number = int(dartResult[i])
                continue
        
        if dartResult[i] == 'S' :
            if dartResult[i] != dartResult[-1] :
                if (ord(dartResult[i+1]) >= 48 and ord(dartResult[i+1]) <= 57) :
                    dartList.append(number)
                    continue
        elif dartResult[i] == 'D' :
            number = number ** 2
            if dartResult[i] != dartResult[-1] :
                if (ord(dartResult[i+1]) >= 48 and ord(dartResult[i+1]) <= 57) :
                    dartList.append(number)
                    continue
        elif dartResult[i] == 'T' :
            number = number ** 3
            if dartResult[i] != dartResult[-1] :
                if (ord(dartResult[i+1]) >= 48 and ord(dartResult[i+1]) <= 57) :
                    dartList.append(number)
                    continue

        if dartResult[i] == '*' :
            number = number * 2
            if dartList == '' :
                dartList.append(number) 
                continue
            else :
                dartList[-1] = dartList[-1] * 2
                dartList.append(number) 
                continue
        elif dartResult[i] == '#' :
            number = -(number)
            dartList.append(number)
            continue

        if i == len(dartResult)-1 :
            dartList.append(number)
          
    return sum(dartList)

# dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
# dartResult = '1D2S3T*'
solution(dartResult)