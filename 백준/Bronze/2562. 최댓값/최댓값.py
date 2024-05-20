List=[]

for i in range(9):
  A=int(input())
  List.append(A)
  
print(max(List))
print(List.index(max(List))+1)