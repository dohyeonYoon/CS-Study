"""
10을 곱할때마다 0이 하나씩 생긴다
10은 2*5 이므로 
2와 5중 더 빈도수가 잦은 수가 몇번 곱해졌는지를 계산

5가 총 몇번 곱해졌는지를 계산 (25에는 5가 두번들어있음)
"""

import math

N = int(input())

def sol(N):
  cnt = 0

  while N != 0:
    N //= 5 
    cnt += N
  return cnt 

print(sol(N))
