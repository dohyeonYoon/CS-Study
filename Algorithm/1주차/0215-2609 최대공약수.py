"""
유클리드 호제법 
두수의 나머지를 이용하여 최대공약수를 찾아나가는 방법
"""
#math.gcd(a,b) 함수 3.9이상
x, y = map(int, input().split())

def gcd(a, b):
  while(b > 0):
    a, b = b, a%b
  return a

res = gcd(x, y)
print(res)
print(x * y // res)