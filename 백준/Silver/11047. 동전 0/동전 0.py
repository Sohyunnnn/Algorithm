N, K= map(int, input().split())

array= []
count=0

for _ in range(N):
  a= int(input())
  array.append(a)

array.sort(reverse=True)

for i in range(N):
    if K // array[i] !=0:
      count+= K // array[i]
      K= K % array[i]

print(count)