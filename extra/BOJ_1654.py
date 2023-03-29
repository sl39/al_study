n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(int(input()))

right = max(mat)
left = 1
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in mat:
        cnt += i//mid
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)