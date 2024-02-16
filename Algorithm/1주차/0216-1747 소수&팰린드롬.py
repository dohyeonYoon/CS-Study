# str[::-1] 로 쉽게 문자 뒤집을 수 있음

import math

def prime(n):
  if n == 1 : 
    return False
  for i in range(2, int(math.sqrt(n)+1)):
    if n % i == 0 : 
      return False
  return True

def palindrome(n):
  if str(n) == str(n)[::-1]:
    return True
  return False

N = int(input())
while True:
  if palindrome(N) and prime(N):
    print(N)
    break
  N += 1
