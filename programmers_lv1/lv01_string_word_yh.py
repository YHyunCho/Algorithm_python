# PROGRAMMAERS LV01 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 작성자 : 조예현
# 최초 작성일 : 2022-07-08
# 최종 작성일 : 2022-07

def solution(s) :
  eng_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  answer = []

  for i in range(len(eng_number)) :
    if eng_number[i] in s :
      s = s.replace(eng_number[i], str(i))

  return int(s)

s = "one4seveneight"
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"

s = solution(s)
print(s)