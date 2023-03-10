n, m = map(int,input().split())
arr = list(map(int,input().split()))


start = 0
end = 0
mys = 0
cnt = 0
while mys < m and start < n:
    mys += arr[start]
    start += 1

while start < n and start >= end:
    if mys == m:
        cnt += 1
        mys -= arr[end]
        end += 1
    if mys < m:
        mys += arr[start]
        start += 1
    if mys > m:
        mys -= arr[end]
        end += 1
    

print(cnt)