arr= ['c=','c-','dz=','d-','lj','nj','s=','z=']

a= input()

for i in arr:
  a= a.replace(i,'*')

print(len(a))