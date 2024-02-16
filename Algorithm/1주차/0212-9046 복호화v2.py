"""
arr = [0]*26 -> 0으로 리스트 초기화해놓고 idx값 하나씩 올리기
ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수 반환 
    ord('?')-ord('a') 몇번째 알파벳인지 
chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환
"""
T = int(input())

for _ in range(T):
    s = input().replace(' ','')
    arr = [0] * 26

    for i in s:
        arr[ord(i)-ord('a')] += 1

    if arr.count(max(arr)) > 1:
        print('?')
    else:
        print(chr(ord('a')+arr.index(max(arr))))
