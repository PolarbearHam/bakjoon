import math
m, n = map(int, input().split())
for i in range(m, n+1):
    error = 0
    if i==0 or i==1:
        error+=1
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            error +=1
            break
    if error==0:
        print(i)