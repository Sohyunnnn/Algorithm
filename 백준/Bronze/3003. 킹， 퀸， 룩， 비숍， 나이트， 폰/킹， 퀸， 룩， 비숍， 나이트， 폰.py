chess=[1,1,2,2,2,8]

List=list(map(int,input().split()))

for i in range(len(chess)):
  chess[i]-=List[i]

for i in range(len(chess)):
  print(chess[i], end=' ')