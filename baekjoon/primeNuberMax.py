import math
m = int(input())
n = int(input())
prime = []
for m in range(m, n+1):
    error = 0
    if m == 0 or m == 1:
        error+=1
    else:
        for i in range(2, int(math.sqrt(m))+1):
            if m%i ==0:
                error+=1
        if error==0:
            prime.append(m)
if len(prime)==0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))