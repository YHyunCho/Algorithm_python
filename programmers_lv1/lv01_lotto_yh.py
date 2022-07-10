# PROGRAMMERS LV01 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

# 작성자 : 조예현
# 최초 작성일 : 2022-07-05
# 최종 작성일 : 2022-07-05

def solution(lottos, win_nums) :

  minimum_nums = 0
  rank = [6, 6, 5, 4, 3, 2, 1]
  rank_num = []

  # for i in lottos :                    
  #   for j in win_nums :
  #     if i == j :
  #       minimum_nums += 1
  #       j = ''                       # To avoid duplication in for loop

  for i in win_nums :                  # Compare the numbers of 'lottos' with list of 'win_nums' except 0
    minimum_nums += lottos.count(i)

  zero = lottos.count(0)               # find 0

  maximum_nums = minimum_nums + zero   

  for i in range(len(rank)) :       # Compare the 'rank' to the 'maximum_nums'
    if maximum_nums == i :
      rank_num.append(rank[i])         

  for i in range(len(rank)) :       # Compare the 'rank' to the 'minimum_nums'
     if minimum_nums == i :
       rank_num.append(rank[i]) 

  return rank_num

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

result = solution(lottos, win_nums)
print(result)