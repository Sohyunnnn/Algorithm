L_list= []
P_list= []
V_list= []

result=0

while(1):
  L,P,V = list(map(int, input().split()))
  if L == 0 and P == 0 and V == 0:
    break
  L_list.append(L)
  P_list.append(P)
  V_list.append(V)



for i in range(len(L_list)):
  count= P_list[i] - L_list[i]
  result= (V_list[i]//P_list[i]) * L_list[i] + min(V_list[i] % P_list[i], L_list[i])
  print("Case %d: %d" %(i+1,result))
    