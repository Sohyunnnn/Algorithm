T=int(input())

List=[0 for i in range(T)]

for i in range(0,T):
    A,B=input().split()
    A=int(A)
    B=int(B)
    List[i]=(A+B)

for i in range(0,T):
  print(List[i])
  