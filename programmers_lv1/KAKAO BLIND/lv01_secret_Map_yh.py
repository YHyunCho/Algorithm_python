# PROGRAMMERS Lv1 [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 작성자 : 조예현
# 최초 작성일 : 2022-07-16
# 최종 작성일 : 2022-07-16

def ChangeBinaryNum (arr, n) :
  Bi_arr = []

  for i in range(n) :
    arr_plus = format(arr[i], 'b')  # 'format' is the function change from integer to binary

    Bi_arr.append(arr_plus)

    if len(Bi_arr[i]) < n :         # if binary num's length is smaller than 'n'
      while len(Bi_arr[i]) != n :   # while It's 'n' in length,
        Bi_arr[i] = '0' + Bi_arr[i] # add a zero in the front

  return Bi_arr

def solution(n, arr1, arr2) :
  answer = []
  Map = []

  arr1_2 = ChangeBinaryNum(arr1, n)
  arr2_2 = ChangeBinaryNum(arr2, n)

  arr1 = []
  arr2 = []

  for i in range(n) :
    arr1 = list(arr1_2[i])    # 'list' is the function divide the list one by one
    arr2 = list(arr2_2[i])

    for j in range(n) :
      if arr2[j] == '1' :     # if second secret map have '1' ,
        arr1[j] = '1'         # change data at first secret map to '1' 
    Map.append(arr1)

  answer = []

  for i in Map :
    for j in range(n) :
      if int(i[j]) == True :  # if integer in map is 1, this is true
        i[j] = '#'            # and change it to '#' too.
      else :                  # if It's false
        i[j] = ' '            # change it to ' '
    i = ''.join(i)
    answer.append(i)

  return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)