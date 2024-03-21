N = int(input())

num_list = []

for i in range(N):
    word = input()
    num = ''
    for j in word:
       
        if j.isdigit():
            num+= j 
        
        else:
            if num:
                num_list.append(int(num))
                num = ''
    
    if num:
        num_list.append(int(num))
num_list.sort()

for i in num_list:
    print(i)

