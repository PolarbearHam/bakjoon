def solution(clothes):
    answer = {}
    for clothe in clothes:
        if clothe[1] in answer: answer[clothe[1]]+=1
        else: answer[clothe[1]] = 1
    cnt = 1
    for i in answer.values():
        cnt*=(i+1)
    return cnt-1
