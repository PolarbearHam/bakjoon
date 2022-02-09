while True:
    arr = input().split()
    if arr == ['0','0','0']:
        break
    if int(arr[0])**2+int(arr[1])**2==int(arr[2])**2:
        print('right')
    else:
        print('wrong')