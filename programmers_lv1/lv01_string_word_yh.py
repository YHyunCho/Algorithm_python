# PROGRAMMAERS LV01 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 작성자 : 조예현
# 최초 작성일 : 2022-07-08
# 최종 작성일 : 2022-07

def solution(s) :
  eng_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  answer = []

  s_len = len(s)

  for i in range(len(eng_number)) :
    for j in range(len(s)) :
      if s[j] == '' :
        break
      elif s[j].isdigit() :
        answer.append(s[j])
        list_s = list(s)
        list_s[j] = ''
        s = ''.join(list_s)
        s = s.ljust(s_len)
        break
      else :
        if s[j:j+2] in eng_number[i] :
          answer.append(eng_number[i])
          len_eng = len(eng_number[i]) +j
          list_s = list(s)
          list_s[j:j+len_eng] = ''
          s = ''.join(list_s)
          s = s.ljust(s_len)
          break
    #print(answer)

  return answer

#s = "one4seveneight"
s = "one4eightseven"
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"

answer = solution(s)