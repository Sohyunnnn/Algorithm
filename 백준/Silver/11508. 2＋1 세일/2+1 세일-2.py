N = int(input())

array= []
count=0

for _ in range(N):
  a= int(input())
  array.append(a)

array.sort(reverse=True)


for i in range(N):
  if (i+1) %3==0:
    continue
  else:
    count+=array[i]

print(count)
