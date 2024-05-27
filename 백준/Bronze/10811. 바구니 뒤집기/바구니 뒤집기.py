N,M=map(int,input().split())


List=[i for i in range(1,N+1)]

temp=0

for u in range(M):
  i,j=map(int,input().split())
  temp=List[i-1:j]
  temp.reverse()
  List[i-1:j]=temp
  
for x in range(N):
  print(List[x])
  