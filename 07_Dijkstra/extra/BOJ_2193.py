n = int(input())
if n == 1 or n == 2:
    print(1)
else:
    arr = [[0,0] for i in range(n)]
    arr[0] = [1,1]
    arr[1] = [1,1]
    for i in range(2,n):
        arr[i][0] = arr[i-1][1]
        arr[i][1] = arr[i-1][0] + arr[i-1][1]

    print(arr[n-1][1])