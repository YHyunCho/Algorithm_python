# PROGRAMMERS Lv1 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 작성자 : 조예현
# 최초 작성일 : 2022-08-18
# 최종 작성일 : 2022-08-18

def solution(participant, completion) :
  participant.sort()
  completion.sort()

  for i in range(len(completion)) :
    if completion[i] != participant[i] :
      return participant[i]

  return(participant[len(completion)])

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
