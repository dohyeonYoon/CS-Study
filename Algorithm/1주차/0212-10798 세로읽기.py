word = []
length = []
str = ""
for i in range(5):
    word.append(input())
    length.append(len(word[i]))

for j in range(max(length)):
    for k in range(5):
        if j < length[k]:
            str += word[k][j]

print(str)