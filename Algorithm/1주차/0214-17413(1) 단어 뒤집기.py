import sys

str = sys.stdin.readline().rstrip()
stack = []
flag = False 
res = ""

for s in str:
  if s == " ":
    while stack:
      res += stack.pop()
    res += s

  elif s == "<":
    while stack:
      res += stack.pop()
    flag = True
    res += s
  
  elif s == ">":
    flag = False
    res += s

  elif flag:
    res += s #태그안에서는 안뒤집음

  else:
    stack.append(s)

while stack:
  res += stack.pop()

print(res)
  