a = input().upper()
b = list(set(a))
arr = []
for i in b:
    count = a.count(i)
    arr.append(count)
if arr.count(max(arr))>1:
    print('?')
else:
    maxi = arr.index(max(arr))
    print(b[maxi])