n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1]
if n == 2:
    print(arr[-1]-arr[0])
else:
    while start < end:
        wifi = arr[0]
        mid = (start + end)//2
        cnt = 1
        for i in range(n):
            if arr[i] - wifi>= mid:
                cnt += 1
                wifi = arr[i]
        
        if cnt >= m:
            result = mid
            start = mid + 1
        else:
            end = mid
    print(result)