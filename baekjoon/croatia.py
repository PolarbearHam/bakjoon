arr = ['c=', 'c-', 'dz=', 'd-',
       'lj','nj', 's=', 'z=']
a = input()
c = 0
for i in arr:
       a = a.replace(i, 'a')
print(len(a))