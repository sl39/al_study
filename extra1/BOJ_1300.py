n = int(input())
m = int(input())

start = 1
end = n**2
res = 1
if m == n*n:
    print(n*n)
else:
    while start < end:
        count = 0
        mid = (start + end)//2
        for i in range(1,n+1):
            count += min(mid//i,n)
        
        if count >= m:
            end = mid
            res = mid
        else:
            start = mid + 1

    print(res)