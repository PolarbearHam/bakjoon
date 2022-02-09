def solution(s):
    answer = ''
    arr = []
    arr = list(map(int, s.split()))
    answer += str(min(arr))+' '+str(max(arr))
    return answer