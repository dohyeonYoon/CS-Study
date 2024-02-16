"""
(1)input() 
str형으로 받음. 
개행 문자 삭제시켜러 줄바꿈없이 출력해 느림
프롬프트메시지를 받아 출력하는 기능이 있어서 속도가 더 느림
입력 값 하나하나 버퍼에 저장
더 이상 입력 없는데 수행되면 EOFError 출력

(2)readline()
str형으로 받음. 개행문자 포함()
[readline().strip() for x in range]
한줄 한번에 버퍼에 저장
.split() 공백 기준 값 나눔
.rstrip() 문자열 끝 공백 제거


"""
import sys
N = int(input())
str = list(map(int, sys.stdin.readline().rstrip()))

print(sum(str))