# https://wook-2124.tistory.com/476 출처

n,m = map(int, input().split())

a = set()
b = set()

for i in range(n):
    a.add(input())

for j in range(m):
    b.add(input())

duplication_name = sorted(list(a&b))
print(len(duplication_name))

for i in duplication_name:
    print(i)
    

