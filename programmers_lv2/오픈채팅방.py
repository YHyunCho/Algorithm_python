def solution(record) :
  uinfo = {}
  result = []

  for i in range(len(record)) :
    record[i] = record[i].split()
    uinfo[record[i][1]] = ''
    
  for i in range(len(record)) :
    if record[i][0] == 'Enter' :
      uinfo[record[i][1]] = record[i][2]
    elif record[i][0] == 'Leave' :
      continue
    else:
      uinfo[record[i][1]] = record[i][2]

  for i in range(len(record)) :
    if record[i][0] == 'Enter' :
      result.append(uinfo[record[i][1]] + '님이 들어왔습니다.')
    elif record[i][0] == 'Leave' :
      result.append(uinfo[record[i][1]] + '님이 나갔습니다.')

  return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = solution(record)