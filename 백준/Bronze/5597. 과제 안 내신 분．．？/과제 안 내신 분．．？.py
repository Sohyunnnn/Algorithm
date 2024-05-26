List=[0]*30


for i in range(30):
  List[i]=i+1
  

for i in range(28):
  k=int(input())
  List.remove(k)

for i in range(len(List)):
  print(List[i])