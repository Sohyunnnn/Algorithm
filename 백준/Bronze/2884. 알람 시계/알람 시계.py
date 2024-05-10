A, B=input().split()

A=int(A)
B=int(B)

if A !=0:
  if B-45>=0:
    print(A,B-45)
  else:
    print(A-1,60+B-45)
else:
  if B-45>=0:
    print(A,B-45)
  else:
    print(23,60+B-45)