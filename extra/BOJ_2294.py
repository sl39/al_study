n,k = map(int,input().split())
coins = []
arr = [k] * (k+10000+1)
for i in range(n):
    c = int(input())
    if c< 10000:
        arr[c] = 1
        coins.append(c)
coins.sort()


for i in range(k):
    for j in coins:
        if arr[i+j] > arr[i] + 1:
            arr[i+j] = arr[i] + 1
if coins[1] != 1 and arr[k] == k:
    print(-1)
else:
    print(arr[k])