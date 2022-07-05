# PROGRAMMERS LV01 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

# 작성자 : 조예현
# 최초 작성일 : 2022-07-04
# 최종 작성일 : 2022-07-04
# 실패한 코드

def Solution(id_list, report, k) :

  report_list = []          # List of divided 'id_list'
  report_men = []           # the users who report
  reported_men =[]          # reported users
  reported_men_list =[]     # List of the users reported more than 'k'
  report_mail_list =[]      # List of the users who received mail
  mail = []                 # the number of received mail by users

  for i in range(0, len(report)) :
    for j in range(i+1, len(report)) :
      if report[i] == report[j] :
        report[j] = ''

  for i in report :
    report_list.extend(i.split())

  for i in range(0, len(report_list)):
    if i % 2 == 0 :
      report_men.append(report_list[i])
    else:
      reported_men.append(report_list[i])

  for i in range(0, len(reported_men)) :
    NumOfReported = 1
    for j in range(i+1, len(reported_men)) :
      if reported_men[i] == reported_men[j] : 
        NumOfReported += 1
    if NumOfReported >= k :
      reported_men_list.append(reported_men[i])

  for i in range(0, len(reported_men_list)) :
    for j in range(0, len(reported_men)) :
      if reported_men_list[i] == reported_men[j] :
        report_mail_list.append(report_men[j])

  mail_num = 0
  for i in range(0, len(id_list)) :
    for j in range(0, len(report_mail_list)) :
      if id_list[i] == report_mail_list[j] :
        mail_num += 1
    mail.append(mail_num)
    mail_num = 0

  return mail

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

result = Solution(id_list, report, k)
print(result)