arr = ['c=', 'c-', 'dz=', 'd-',
       'lj','nj', 's=', 'z=']
a = input()
c = 0
stack = ''
for i in a:
       stack += i
       if stack in arr:
              stack
       else:
              c+=1
print(c)