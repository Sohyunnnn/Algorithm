import sys

A=1
B=1

while True:
  try:
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)
  except:
    break