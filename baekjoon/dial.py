a = input()
answer = 0
for i in a:
    if 0<=ord(i)-65<3:
        answer += 3
    elif 3<=ord(i)-65<6:
        answer += 4
    elif 6<=ord(i)-65<9:
        answer += 5
    elif 9<=ord(i)-65<12:
        answer += 6
    elif 12<=ord(i)-65<15:
        answer += 7
    elif 15<=ord(i)-65<19:
        answer += 8
    elif 19<=ord(i)-65<22:
        answer += 9
    elif 22<=ord(i)-65<26:
        answer += 10
print(answer)