n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

dp = [[1e9]*(1<<n) for i in range(n)]


dp[0][1] = 0
for j in range(1<<n):
    for i in range(n):
        if dp[i][j] == 1e9:
            continue
        for k in range(n):
            if j&(1<<k):
                continue
            if mat[i][k] == 0:
                continue
            
            dp[k][j|(1<<k)] = min(dp[k][j|(1<<k)],dp[i][j]+mat[i][k])



res = 1e9
for i in range(n):
    if mat[i][0]:
        res = min(res, mat[i][0] + dp[i][(1<<n)-1])

print(res)