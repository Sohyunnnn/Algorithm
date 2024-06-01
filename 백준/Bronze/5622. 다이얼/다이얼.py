STR=input()

dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

ret=0

for i in range(len(STR)):
  for j in dial:
    if STR[i] in j:
      ret+=dial.index(j)+3
      
print(ret)