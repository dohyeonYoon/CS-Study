'''
아이디어
- 문자열을 하나씩 스택에 삽입하고 "("와 ")"이 만날 때 pop 
'''

n = int(input())

for _ in range(n):
    text = input()
    stack = []

    for t in text:
        if not stack: # 만약 stack이 비어있다면 현재 문자를 stack에 삽입
            stack.append(t)
        elif stack[-1]=="(" and t==')': # 만약 stack의 마지막 요소가 "("이고, 현재 문자가 ")"이라면 stack의 마지막 요소 pop
            stack.pop()
        else: # 그외의 경우 stack에 삽입
            stack.append(t)

    if stack: # 만약 stack이 비어있지 않다면(괄호 짝이 맞지 않다면)
        print("NO")
    else: # 만약 stack이 비어있다면(괄호 짝이 맞다면)
        print("YES")