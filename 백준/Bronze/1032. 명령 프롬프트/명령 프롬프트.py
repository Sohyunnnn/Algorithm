N = int(input())
arr= []

arr = [input() for _ in range(N)]

result = ""

for chars in zip(*arr):  
  if all(c == chars[0] for c in chars):
    result+= chars[0]
  else:
    result+="?"

print(result)