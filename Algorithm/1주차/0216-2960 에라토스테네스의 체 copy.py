"""
에라토스테네스의 체 = N보다 작거나 같은 모든 소수를 찾기

#1 리스트

def listPrime(n):
  primes = []
  list = [False, False] + ([True] * (n - 1))

  for i in range(2, N + 1):
    if list[i]:
      primes.append(i)
    for j in range(i * 2, N + 1, i):
      list[j] = False
  
  return primes

#2 집합 set
def setPrime(n):
    num = set(range(2, n+1)) # 2부터 n까지의 집합

    for i in range(2, n+1): 
        if i in num: # i가 num에 있으면
            num-=set(range(2*i,n+1,i)) # 집합 num에서 i의 배수 제외
    return num

#3 제곱근함수 sqrt (소수여부판단)
import math
def isPrime(n):
    if n==1: # 1은 약수가 아니므로 제외
        return False
    else:
        print(math.sqrt(5))
        for i in range(2,int(math.sqrt(n))+1): # n의 제곱근까지 약수가 존재하는지 확인
            if n%i==0: # 약수가 존재하면 False
                return False
        return True # 존재하지 않으면 True
"""

N, K = map(int, input().split())
cnt = 0
list = [True]* (N + 1)

for i in range(2, N+1):
  for j in range(i, N+1, i):
    if list[j] != False:
      list[j] = False 
      cnt += 1

      if(cnt == K): print(j)