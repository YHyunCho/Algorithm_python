# PROGRAMMERS Lv1 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 작성자 : 조예현
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-24

def solution(board, moves):
  answer = 0
  crane = []

  for i in board :
    i.insert(0, 0)

  for i in moves :
    for j in board :

      if j[i] == 0 :
        continue
      else : 
        crane.append(j[i])
        j[i] = 0

        if len(crane) >= 2 : 
          if crane[-1] == crane[-2] :
            del crane[-2:]
            answer += 2

        break

  return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
solution(board, moves)