H, M= input().split()

H= int(H)
M= int(M)

T=int(input())

if T+M>=60:
  H=(T+M)//60+H
  M=(T+M)%60
  if H>23:
    H=H-24
else:
  M=T+M
  
print(H,M)