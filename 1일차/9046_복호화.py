T = int(input())
 
for _ in range(T):
    s = input().replace(' ', '')
    count_s = [0] * 26
 
    for i in s:
        count_s[ord(i) - 97] += 1
 
    if count_s.count(max(count_s)) > 1:
        print('?')
    else:
        print(chr(97 + count_s.index(max(count_s))))


# 다시 짜보기
# N = int(input())
# alpha = []
# alpha_list = []
# for a in range(0,26):
#     alpha.append( chr(97+a))


# for a in range(N):
#     word = list(input().replace(' ',''))
#     for i in range(len(alpha)):
#         cnt = 0
#         for j in word:
#             if alpha[i] in j:
#                 cnt += 1
#         alpha_list.append(cnt)
#     if alpha_list.count(max(alpha_list)) > 1 :
#         print(alpha_list)
#     else:
#         print("dd",alpha_list)