# PROGRAMMAERS LV01 직사각형 별찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/12969

# 작성자 : 조예현
# 최초 작성일 : 2022-07-10
# 최종 작성일 : 2022-07-10

# input a, b
a, b = map(int, input().strip().split(' '))

# Enter a row to use for loops
for i in range(b) :
  # Enter a columns to use for loops
  for j in range(a) :
    # Print '*'
    print('*', end='', sep='')
  print()