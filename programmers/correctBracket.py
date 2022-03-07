def solution(s):
    answer = []
    stack = []
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack==[]:
                return False
            else:
                stack.pop()
    return stack==[]