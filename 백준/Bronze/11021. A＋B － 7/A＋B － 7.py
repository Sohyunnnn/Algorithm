import sys

T=int(input())

for i in range(0,T):
  A,B=map(int, sys.stdin.readline().split())
  print('Case #%d: %d' %(i+1,A+B))