n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

left = min(arr)
right = sum(arr)
mx = max(arr)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    money = 0
    for i in range(n):
        if arr[i] > money:
            money = mid
            cnt += 1
        money -= arr[i]

    
    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(right+1)