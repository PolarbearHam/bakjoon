a = list(map(str, input().split()))
b = ''.join(reversed(a[0]))
c = ''.join(reversed(a[1]))
if b>c:
    print(b)
else:
    print(c)
