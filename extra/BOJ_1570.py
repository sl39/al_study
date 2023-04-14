arr = list(map(int,input().split()))
if arr[1] > arr[3] or arr[2] > arr[4]:
    print(-1)
    exit()
    
if arr[4] - arr[2] + arr[3] - arr[1] <= arr[0]:
    print((arr[3] - arr[1])*'R' + (arr[4] - arr[2])*'U'+(arr[0]-(arr[4] - arr[2] + arr[3] - arr[1]))*'R')
    exit()

