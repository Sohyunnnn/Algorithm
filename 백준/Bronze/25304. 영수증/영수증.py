X=int(input())

N= int(input())

A=[]

B=[]

total=0

for i in range(0,N):
  a, b =map(int, input().split())
  A.append(a)
  B.append(b)
  
for i in range(0,N):
  total+= A[i]*B[i]

if total == X:
  print('Yes')
else:
  print('No')