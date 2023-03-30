n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
    
right = 0
mys = 0
for i in mat:
    right = max(right,max(i))
    mys += sum(i)
left = 1
ans = 0
while left <= right:
    mid = (right+left)//2
    cnt = 0
    for i in mat:
        for j in i:
            cnt += min(mid,j)
    
    if 2*cnt >= mys:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
        
if n == 1:
    if mat[0][0]//2 < mat[0][0]/2:
        print(mat[0][0]//2 + 1)
    else:
        print(mat[0][0]//2)
else:
    print(ans)