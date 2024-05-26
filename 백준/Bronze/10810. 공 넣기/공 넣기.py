N,M=map(int,input().split())

List= [0 for i in range(N)]


for u in range(M):
  i,j,k= list(map(int, input().split()))
  
  for u in range(i-1,j):
    List[u]=k 

for i in range(N):
  print(List[i])