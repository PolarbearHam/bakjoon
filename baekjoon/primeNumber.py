import math
n = int(input())
count =0
arr = list(map(int, input().split()))
for i in arr:
    error = 0
    if i==0 or i==1:
        error += 1
    else:
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                error += 1
        if error ==0:
            count+=1
print(count)