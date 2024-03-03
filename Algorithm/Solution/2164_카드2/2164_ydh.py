'''
아이디어
1158번이랑 비슷, 요세프스 문제와 같이 큐 활용 
'''

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])

        
        
        