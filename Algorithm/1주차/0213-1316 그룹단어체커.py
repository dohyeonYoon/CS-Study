import sys

n = int(input())
cnt = n

for _ in range(n) :
    word = sys.stdin.readline()
    for i in range(len(word)-1) :
        #aaaa 와같이 연속하는 동안은 pass
        if word[i] == word[i+1] :
            pass
        #aaaab 달라지는 시점에서 in 함수 사용. 그룹단어가 아님
        elif word[i] in word[i+1:] :
            cnt -= 1
            break

print(cnt)