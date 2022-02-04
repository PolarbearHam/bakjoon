# import math
# def is_prime_number(num):
#     if num==0 or num==1:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num%i==0:
#             return False
#     return True
# n = int(input())
# count = 2
# if n==1:
#     exit()
# while n>1:
#     if n%count==0 and is_prime_number(count):
#         n=n/count
#         print(count)
#     else:
#         count+=1
n = int(input())
count = 2
while n!=1:
    if n%count == 0:
        n = n/count
        print(count)
    else:
        count+=1