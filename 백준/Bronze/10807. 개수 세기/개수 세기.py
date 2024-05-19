N= int(input())


List = list((map(int, input().split())))

V= int(input())

count=0

for i in range(0,N):
  if V==List[i]:
    count+=1
    
print(count)