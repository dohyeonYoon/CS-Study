'''
아이디어
스택으로 문제 해결
'('은 그냥 스택에 넣는다
')'가 나오면 두가지 경우로 나눈다
')'가 나오고 이전 문자가 '('이었다면 이부분은 레이저이다. 따라서 stack에 쌓인 '(' 개수(=쇠막대기)만큼 카운트를 더한다
')'가 나오고 이전 문자가 ')'이었다면 쇠막대기 끄트머리이다. 따라서 하나가 나올때마다 하나만 카운트를 한다
'''

text = list(input())
count = 0
stack = []
for i in range(len(text)): 
    
    if text[i] =='(': # '('가 나오는 경우 1가지  
        stack.append('(')
    
    else: # ')'가 나오는 경우 2가지
        if text[i-1] == '(': # 이전 문자가 '('이므로 레이저 부분
            stack.pop()
            count += len(stack)
        
        else: # 이전 문자가 ')'이므로 쇠막대기 끄트머리 부분
            stack.pop()
            count += 1

print(count)
        
        