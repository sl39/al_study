n = int(input())
arr = list(map(int,input().split()))

arr.sort()
mn = 2000000000
start = 0
end = n-1
a = 0
b = 0
while start < end:
    cnt = arr[start] + arr[end]
    if mn > abs(cnt):
        a = arr[start]
        b = arr[end]
        mn = abs(cnt)
    if cnt == 0:
        break
    if cnt < 0:
        start += 1
    else:
        end -= 1

print(a,b)