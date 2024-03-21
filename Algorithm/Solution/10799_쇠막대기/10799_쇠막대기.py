bar_razor = list(input())
answer = 0
stack = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(': 
        stack.append('(')
        
    else:
        # ) 직전이 ( 경우 pop 하고 막대 갯수 추가
        if bar_razor[i-1] == '(': 
            stack.pop()
            answer += len(stack)
        # 막대의 끝인 경우
        else:
            stack.pop() 
            answer += 1 

print(answer)