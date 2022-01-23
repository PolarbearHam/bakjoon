a = int(input())
for i in range(a):
    b = input()
    back =[]
    for j in b:
        if j == "(":
            back.append(j)
        elif j == ")":
            if len(back) != 0 and back[-1] == "(":
                back.pop()
            else:
                back.append(")")
                break
    if len(back) == 0:
        print("YES")
    else:
        print("NO")