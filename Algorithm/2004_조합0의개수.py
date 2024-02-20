import sys
a,b = map(int, sys.stdin.readline().split())

# 2와 5의 개수세기 (m 자리에 2, 5)
def count(n, m):
   if n < m:
       return 0
   
   count = 0
   while n >= m:
       count += n // m
       n = n // m
   return count

two_count = count(a,2) - count(a-b,2) - count(b,2)
five_count = count(a,5) - count(a-b,5) - count(b,5)
print(min(two_count, five_count))
