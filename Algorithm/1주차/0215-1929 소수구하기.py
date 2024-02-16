#에라토스테네스의 체(소수구하기)
#M~N만큼의 배열 해당 인덱스값으로 초기화
#2부터 시작해서 2의배수,3의배수,4의배수 지워나감
#2의제곱근 3의제곱근 지워나가도 상관 x

M, N = map(int, input().split())

prime = [True]*(N+1)
prime[0] = False
prime[1] = False

for i in range(2, int(N**0.5)+1):
  if prime[i]:
    for j in range(i*2, N+1, i):
      prime[j] = False

for i in range(M, N+1):
  if prime[i]:
    print(i)