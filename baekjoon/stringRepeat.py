t = int(input())
arr = []
for _ in range(t):
     arr.append(list(map(str, input().split())))
answer = ''
for i in range(len(arr)):
    for j in range(len(arr[i][1])):
        answer += arr[i][1][j]*int(arr[i][0])
    print(answer)
    answer = ''
