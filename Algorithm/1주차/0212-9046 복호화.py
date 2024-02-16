"""
사전 정렬 : sorted(dict.values(), reverse=True)
최댓값 가지는 키 찾기 : max(dict, key=dict.get)

"""
import sys
N = int(input())

for i in range(N):
    sentence = list(sys.stdin.readline().rstrip())
    dic_freq = dict()

    for j in sentence:
        if j != " ":
            if j not in dic_freq:
                dic_freq[j] = 1
            else:
                dic_freq[j] += 1

    dic = sorted(dic_freq.values(), reverse=True)

    if(len(dic) > 1 and dic[0] == dic[1]) or len(dic) == 0:
        print("?")
    else:
        print(max(dic_freq, key=dic_freq.get))