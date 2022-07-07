# PROGRAMMERS LV01 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

# 작성자 : 조예현
# 최초 작성일 : 2022-07-05
# 최종 작성일 : 2022-07-07
from collections import defaultdict

def solution(id_list, report, k) :

  reported_dict = defaultdict(int)     
  report_dict = defaultdict(set)
  answer = []
  report = list(set(report))

  for i in report :
    a,b = i.split()
    report_dict[a].add(b)
    reported_dict[b] += 1

  for i in id_list :
    result = 0
    for j in report_dict[i] :
      if reported_dict[j] >= k :
        result += 1
    answer.append(result)
  
  return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

result = solution(id_list, report, k)
print(result)