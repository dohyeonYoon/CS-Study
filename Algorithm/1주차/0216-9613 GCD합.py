import sys
t = int(input())

def gcd(a, b):
  while(b != 0):
    a, b = b, a % b
  return a

for i in range(t):
  li = list(map(int, sys.stdin.readline().split()))
  sum = 0
  
  for j in range(1, li[0]):
    for k in range(j + 1, li[0]+1):
      sum += gcd(li[j], li[k])

  print(sum)  
    