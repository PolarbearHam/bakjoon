a = input()
b = [-1 for _ in range(26)]
for i in range(len(a)):
    if b[ord(a[i])-97]==-1:
        b[ord(a[i])-97]=i
answer = ''
for i in range(len(b)):
    answer += str(b[i])+' '
print(answer)