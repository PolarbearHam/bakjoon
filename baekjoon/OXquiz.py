a = int(input())
n = []
for i in range(a):
    n.append(input())
count = 0
answer = 0
for j in range(len(n)):
    for k in range(len(n[j])):
        if n[j][k]=='O':
            if count == 0:
                count +=1
                answer +=1
            else:
                count +=1
                answer = answer+count
        else:
            count = 0
    print(answer)
    answer = 0
    count = 0