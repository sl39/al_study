n,k = map(int,input().split())

arr = [int(input()) for i in range(n)]

i = n-1
cnt = 0
while i >-1:
    if arr[i] > k:
        pass
    else:
        cnt += k //arr[i] 
        k = k %arr[i]
    i -= 1
    if k == 0:
        break

print(cnt)
