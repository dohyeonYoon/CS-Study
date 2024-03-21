from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)  
        front = queue.popleft() 
        m -= 1 #위치가 한 칸 당겨짐

        if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
            count += 1
            if m < 0: 
                print(count)
                break

        else: #제일 큰 숫자가 아닐 때
            queue.append(front) 
            if m < 0 : 
                m = len(queue) - 1 