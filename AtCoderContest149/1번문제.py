# X는 10^n 보다 작은 양의 정수입니다. 
# 그리고 X의 모든 자리수 숫자는 같습니다.
# X는 M의 배수입니다. 
# 조건을 만족하는 양의 정수 X가 없으면 -1을 인쇄합니다.

# input : N = 7, M = 12
# 4개의 양의 정수 X는 444,888,44444,88888의 조건을 만족합니다. 정답은 그 중 최대치인 88888입니다.

n,m=map(int,input().split())
mx=[0,0]
for i in range(1,10):
  tmp=0
  for j in range(1,n+1):
    tmp=tmp*10+i
    tmp%=m
    if tmp==0:
      mx=max(mx,[j,i])
 
if mx[0]!=0:
  print(str(mx[1])*mx[0])
else:
  print(-1)