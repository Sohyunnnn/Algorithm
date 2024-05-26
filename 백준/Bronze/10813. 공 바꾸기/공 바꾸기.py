N,M =map(int, input().split())

List=[0]*N

for u in range(0,N):
  List[u]=u+1

for u in range(M):
  i,j=map(int,input().split())
  
  a= List[i-1]
  List[i-1]=List[j-1]
  List[j-1]=a
  
for u in range(N):
  print(List[u])