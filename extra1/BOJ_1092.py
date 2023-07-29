n = int(input())
crains = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))
crains.sort()
box.sort()
arr = [0] * n
start = 0
now = 0
while start < m and now < n:
    if crains[now] < box[start]:
        now += 1
    else:
        arr[now] += 1
        start += 1
if now == n:
    print(-1)
else:
    end = n-1
    count = arr[-1]
    mx = arr[-1]
    start = 1
    while end > 0:
        start += 1
        count += arr[end-1]
        if mx <= arr[end-1]:
            if count % start:
                arr[end-1] = count//start  + 1
            else:
                arr[end-1] = count//start
            mx = max(arr[end-1],mx)
        end -= 1
    print(mx)