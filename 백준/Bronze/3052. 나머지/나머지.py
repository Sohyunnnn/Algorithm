List= [0]*10

for i in range(10):
  List[i]=int(input())
  
for i in range(10):
  List[i]=List[i]%42
  
print(len(set(List)))