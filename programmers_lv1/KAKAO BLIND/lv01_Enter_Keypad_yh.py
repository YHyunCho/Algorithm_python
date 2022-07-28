# PROGRAMMERS Lv1 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# 작성자 : 조예현
# 최초 작성일 : 2022-07-26
# 최종 작성일 : 2022-07-26

def solution(numbers, hand):
    answer = ''
    keypad = {1: [0,0], 2: [0,1], 3: [0,2],
              4: [1,0], 5: [1,1], 6: [1,2],
              7: [2,0], 8: [2,1], 9: [2,2],
              '*': [3,0], 0: [3,1], '#': [3,2]}
    LastEnter = ['*', '#']

    for i in numbers :

      if i == 1 or i == 4 or i == 7:
        answer += 'L'
        LastEnter[0] = i

      elif i == 3 or i == 6 or i == 9 :
        answer += 'R'
        LastEnter[1] = i
        
      else :

        Left = abs(keypad[LastEnter[0]][0] - keypad[i][0]) + abs(keypad[LastEnter[0]][1] - keypad[i][1])
        Right = abs(keypad[LastEnter[1]][0] - keypad[i][0]) + abs(keypad[LastEnter[1]][1] - keypad[i][1])

        if Left < Right :
          answer += 'L'
          LastEnter[0] = i
        elif Left > Right :
          answer += 'R'
          LastEnter[1] = i
        else :
          if hand == 'right' :
            answer += 'R'
            LastEnter[1] = i
          else :
            answer += 'L'
            LastEnter[0] = i

    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = 'right'
solution(numbers, hand)