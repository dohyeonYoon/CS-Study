'''
아이디어
nCr = n!/(n-r)!r! 이라는 공식을 활용
2의 지수 = n!의 2의 지수 - (n-r)!의 2의 지수 - r!의 2의 지수
5의 지수 = n!의 5의 지수 - (n-r)!의 5의 지수 - r!의 5의 지수
1676번(팩토리얼 0의 개수)과 마찬가지로 2의 지수와 5의 지수중 작은 값이 답
정수 n,m (0<=m<=n<=2,000,000,000, n!=0)
'''

from sys import stdin

n, m = map(int, stdin.readline().split()) # 공백을 기준으로 n,m 받아오기

def count2(N): # 입력값의 소인수 분해 중 2의 개수 카운트
    if N < 2: # 입력값이 2보다 작으면 0 반환
        return 0
    
    count = 0
    while N >= 2: 
        count += N//2 # 입력값을 2로 나눈 몫을 더하기
        N = N//2 # 2의 배수인 경우도 포함할 수 있음 ex) 4,8,16
    return count

def count5(N): # 입력값의 소인수 분해 중 5의 개수 카운트
    if N < 5: # 입력값이 5보다 작으면 0 반환
        return 0
    
    count = 0
    while N >= 5:
        count += N//5 # 입력값을 5로 나눈 몫을 더하기
        N //= 5 # 5의 배수인 경우도 포함할 수 있음 ex) 5,25,125
    return count

two_count = count2(n) - count2(n-m) - count2(m)
five_count = count5(n) - count5(n-m) - count5(m)
print(min(two_count, five_count))