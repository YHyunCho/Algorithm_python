def Solution(id_list, report, k) :
  report_list = []
  report_men = []
  reported_men =[]
  for i in report :
    report_list.extend(i.split())
  for j in range(0, len(report_list)):
    if j % 2 == 0 :
      report_men.append(report_list[j])
    else:
      reported_men.append(report_list[j])


  print(report_men)
  print(reported_men)
  return report_list

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

result = Solution(id_list, report, k)