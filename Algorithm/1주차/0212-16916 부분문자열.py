"""
KMP알고리즘 : 
특정글에서 하나의 문자열을 찾는 문자열 매칭 알고리즘 중 하나
찾고자 하는 문자열에서 가장 길게 겹치는 부분을 찾아
겹치는 길이만큼 스킵하며 찾아서
시간복잡도가 (N)
"""
"""
1.두개의 포인터 i, j를 가지고 비교
2.문자열이 몇번째 인덱스까지 같은지에 대한 정보를 저장하는 값으로 테이블만듬
3.해당 테이블을 KMP 알고리즘에서 사용 

3.일치하지 않는 j인덱스의 한칸 전 인덱스 값을 가져옴
4.일치하지 않았던 i인덱스 문자와 한칸 뒤로 옮긴 j인덱스 문자만 비교. 
5.비교하는 j인덱스 전의 문자들은 비교할 이유가없음(이미 일치함을 알기 때문)



"""
import sys 

def makeTable(pattern):
  patternSize = len(pattern)
  table = [0] * patternSize #접두-접미사가 일치하는 길이를 표현하는 테이블 생성
  j = 0 #일치하는 최대문자열 길이를 나타내는 값
  for i in range(1, patternSize):
    while(j > 0 and pattern[i] != pattern[j]):
      j = table[j-1]
    if(pattern[i] == pattern[j]):
      j += 1
      table[i] = j

  return table

#일치했던 부분까지 되돌아가서 다시 검사하는 방식으로 빠르게 최대 일치 길이 테이블을 구축하기 위함
def KMP(parent, pattern):
  table = makeTable(pattern)
  parentSize = len(parent)
  patternSize = len(pattern)
  j = 0
  flag = False

  for i in range(0, parentSize):
    while(j > 0 and parent[i] != pattern[j]):
      j = table[j-1] 
    if parent[i] == pattern[j]:
      if(j == patternSize -1):
        flag = True #True 나온 시점에서 스킵해도됨.
        j = table[j] 
      else:
        j += 1

  return flag

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

if KMP(S, P): 
  print(1) 
else: 
  print(0)