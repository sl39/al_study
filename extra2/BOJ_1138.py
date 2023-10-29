n = int(input())

arr = list(map(int,input().split()))
ans = [0]*n

for i in range(n):
    t = 0
    cnt = 0
    for j in range(arr[i]):
        if ans[j] == 0:
            cnt += 1
    while ans[arr[i]+t] != 0 or cnt != arr[i]:
        if ans[arr[i]+ t] == 0:
            cnt += 1
        t += 1
    ans[arr[i]+t] = i + 1

print(*ans)