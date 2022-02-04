import sys
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
all_num = [x for x in range(123456*2+1)]
prime_list = []
for i in all_num:
    if is_prime(i):
        prime_list.append(i)
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    count = 0
    for i in prime_list:
        if n < i <= 2*n:
            count +=1
    print(count)