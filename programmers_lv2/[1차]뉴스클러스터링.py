import math

def strCheck(s) :

  s = s.lower()
  s = [s[i:i+2] for i in range(len(s)-1)]
  s = [i for i in s if i.isalpha()]

  return s

def setIntersection(str1, str2) :
  set1 = []
  
  for i in range(len(str1)):
    for j in range(len(str2)) :
      if str1[i] == str2[j] :
        set1.append(str1[i])
        str1[i] = 0
        str2[j] = -1
        continue

  return set1

def solution(str1, str2) :

  s1 = strCheck(str1)
  s2 = strCheck(str2)
  if len(s1) == 0 and len(s2) == 0 :
    return 65536

  set1= setIntersection(s1, s2)
  lenSet2 = len(s1) + len(s2) - len(set1)
  J = (len(set1) / lenSet2) * 65536
  
  return math.trunc(J)

str1, str2 ='handshake', 'shake hands'
# str1, str2 = 'aa1+aa2', 'AAAA12'
# str1, str2 = 'FRANCE', 'french'
answer= solution(str1, str2)
print(answer)