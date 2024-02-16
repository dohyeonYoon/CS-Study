#리스트를 문자열로 합쳐줌 ''.join / 앞의 ''는 구분자를 뭘줄건지
s = input()

tmp = []
result = []

for i in range(len(s)):
    if s[i] == '>':
        tmp.append('>')
        result.append(''.join(tmp))
        tmp = []
    elif s[i] == '<' and tmp:
        tmp.reverse()
        result.append(''.join(tmp))
        tmp = [s[i]]
    elif s[i] == ' ' and '<' not in tmp:
        tmp.reverse()
        result.append(''.join(tmp))
        result.append(' ')
        tmp = []
    else:
        tmp.append(s[i])

if tmp:
    tmp.reverse()
    result.append(''.join(tmp))

print(''.join(result))