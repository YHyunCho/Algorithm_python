# PROGRAMMERS Lv1 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 작성자 : 조예현
# 최초 작성일 : 2022-07-24
# 최종 작성일 : 2022-07-24

def solution(new_id):
    answer = ''

    # step1
    new_id = new_id.lower()
    new_id = list(new_id)

    # step2
    for i in range(len(new_id)) :
      if ((ord(new_id[i]) >= 97 and ord(new_id[i]) <= 122) or
          (ord(new_id[i]) >= 48 and ord(new_id[i]) <= 57) or 
          new_id[i] =='-' or new_id[i] =='_' or new_id[i] == '.') :
            answer += new_id[i]

    # step3
    while answer.find('..') != -1 :
      answer = answer.replace('..', '.')

    # step4
    #answer = list(answer)
    if answer.find('.') == 0 : 
      answer = answer[1:]  

    if answer.rfind('.') == len(answer)-1 : 
      answer = answer[:len(answer)-1]

    # step5
    if answer == '' :
      answer = 'a'

    # step6
    print(len(answer))
    if len(answer) >= 16 :
      answer = answer[:15]
      if answer.rfind('.') == len(answer)-1 : 
        answer = answer[:len(answer)-1]

    # step7
    if len(answer) <= 2 :
      while len(answer) != 3 :
        answer += answer[-1]

    return answer

#new_id = "...!@BaT#*..y.abcdefghijklm"
#new_id = "z-+.^."
#new_id = "=.="
#new_id = "123._def"
new_id = "abcdefghijklmn.p"
solution(new_id)