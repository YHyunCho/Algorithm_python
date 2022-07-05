# PROGRAMMERS LV01 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

# 작성자 : 조예현
# 최초 작성일 : 2022-07-05
# 최종 작성일 : 2022-07-

def solution(id_list, report, k) :

  report_list = []          # List of divided 'report'
  report_dict = dict()
  answer = []

  for i in range(len(report)) :
    for j in range(i+1, len(report)) :
      if report[i] == report[j] :
        report[j] = ''

  for i in range(len(id_list)):
    report_dict[id_list[i]] = []
  for i in report :
    if i == '' :
      continue
    report_list.append(i.split())

  report = []

  for j in range(len(report_list)) :
    num = 1
    for h in range(len(report_list)) :
      if j != h and report_list[j][1] == report_list[h][1] :
        num += 1
    if num >= k :
      report.append(report_list[j])

  for i in report_dict.keys() :
    for j in range(len(report)) :
      if report[j][0] in i :
        report_dict[i].append(report[j][1])

  for i in report_dict.keys() :
    answer.append(len(report_dict[i]))

  return (answer)


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

result = solution(id_list, report, k)
print(result)