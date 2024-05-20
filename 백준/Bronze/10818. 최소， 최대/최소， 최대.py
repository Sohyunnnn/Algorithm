N= int(input())

List= list(map(int, input().split()))

Max= List[0]

Min= List[0]

for i in range(0,N):
  if Max <= List[i]:
    Max=List[i]
  if Min >= List[i]:
    Min= List[i]
    
print(Min, Max)
