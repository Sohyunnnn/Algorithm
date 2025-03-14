
N = int(input())
string = input()

count = string.count("LL")

if count <= 1:
  print(N)
else:
  print(N-count+1)

