A,B,C,M = map(int, input().split())

count= 0
total=0

for _ in range(24):
    if total + A <= M:
      count+=1
      total+=A
    else:
      total-=C
      if total < 0:
            total = 0

print(count*B)