n,d,k,c = map(int,input().split())
check = [0] * (d+1)
arr = []
for i in range(n):
    arr.append(int(input()))
cnt = 0
for i in range(k):
    if not check[arr[i]]:
        cnt += 1
    check[arr[i]] += 1

if check[c] == 0:
    cnt += 1

start = 0
for end in range(k,n):
    if check[end] == 0:
        cnt += 1
    check[end] += 1
    