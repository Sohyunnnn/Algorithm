N = int(input())

coin = 1000

res = coin - N

count =0 

while(1):
  if res //500 >= 1 :
    count += res//500
    res= res%500

  elif res //100>=1:
    count += res//100
    res= res%100
  elif res //50>=1:
    count += res//50
    res= res%50
  elif res //10>=1:
    count += res//10
    res= res%10
  elif res //5>=1:
    count += res//5
    res= res%5
  else:
    count += res//1
    res= res%1
    break

print(count)

