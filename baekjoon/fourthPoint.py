A = input().split()
B = input().split()
C = input().split()
D = []
for i in range(2):
    if A[i]==B[i]:
        D.append(C[i])
    elif A[i]==C[i]:
        D.append(B[i])
    else:
        D.append(A[i])
answer = str(D[0])+' '+str(D[1])
print(answer)
