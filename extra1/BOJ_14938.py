n,m,l = map(int,input().split())

arr= list(map(int,input().split()))

mat = [[1e9]*n for i in range(n)]
for i in range(l):
    a,b, cost = map(int,input().split())
    mat[a-1][b-1] = cost
    mat[b-1][a-1] = cost

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j==k:
                continue
            mat[j][k] = min(mat[j][k],mat[j][i] + mat[i][k])

mx = 0
for i in range(n):
    res = arr[i]
    for j in range(n):
        if mat[i][j] <= m:
            res += arr[j]
    mx = max(mx,res)

print(mx)
    