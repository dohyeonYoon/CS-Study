N = int(input())

cnt = 1

for i in range(N):
    cnt += i * 6
    if cnt >= N:
        print(i+1)
        break