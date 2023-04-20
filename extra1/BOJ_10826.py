n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]

    print(arr[-1])