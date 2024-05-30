N=int(input())

hap=0

score = list(map(int, input().split()))

top=max(score)

for i in range(N):
  score[i]=score[i]/top*100
  hap+=score[i]
  
print(hap/N)