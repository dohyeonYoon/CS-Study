'''
아이디어
디큐를 활용하여 원형 큐를 만든다
'''

from collections import deque
n, k = map(int, input().split())
people = deque()

# 원형큐 생성
for i in range(1, n+1):
   people.append(i)

result = []
while people: # 큐가 비어 있을 때까지 반복
  for _ in range(k-1): # k-1번째까지 사람들을 왼쪽에서 오른쪽으로 이동
    people.append(people.popleft())


  result.append(people.popleft()) # k번째 사람을 큐에서 제거하고 결과 리스트에 추가

print(str(result).replace('[', '<').replace(']', '>'))
    
'''
예시
n=7, k=3
[ O O O O O O O ]
[ O O X O O O O ]
[ O O X O O O O]

'''        

        