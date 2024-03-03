'''
아이디어
deque를 이용하여 첫번째 원소 빼고 마지막에 append
첫번째 문서의 인덱스와 중요도를 변수에 저장 후 조건 체크한 뒤 처리
'''

from collections import deque
from sys import stdin

t = int(stdin.readline().strip()) # 문서의 갯수

for _ in range(t):
    que = deque()
    n,m = map(int, stdin.readline().strip().split()) # 문서 갯수 n, 궁금한 문서의 인덱스 m
    impo = list(map(int,stdin.readline().strip().split())) # n개 문서 중요도
    
    # 큐에 인덱스,중요도 저장
    for idx, imp in enumerate(impo):
        que.append((idx,imp))
    
    # 인덱스 저장 후 중요도에 따라 정렬 
    impo.sort() # 오름차순
    count = 0
    
    while(que):
        idx, imp = que.popleft() # 첫번째 문서 인덱스, 중요도 빼서 저장
        
        if imp == impo[-1]: # 첫번째 문서의 중요도가 전체에서 제일 큰가?
            impo.pop()
            count +=1
            
            if idx == m: # 첫번째 문서의 인덱스가 m과 같은가?
                print(count)
                break
        
        else:
            que.append((idx,imp)) # 아니라면 뒤에 삽입