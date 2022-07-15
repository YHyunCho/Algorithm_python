def solution(n) :
  answer = ''
  watermelon = '수박'

  len_watermelon = int(n / 2)

  for i in range(len_watermelon) :
    answer += watermelon

  if n % 2 == 1 :
    answer += '수'

  return answer

n = 3
n = 4
solution(n)