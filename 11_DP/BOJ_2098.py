n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

dp = [[1e9]*(1<<n) for i in range(n)]

def dfs(x,path):
    if path == (1<<n) - 1:
        if mat[x][0]:
            dp[0][path] = min(dp[0][path], dp[x][path]+mat[x][0])
        return
    
    # if dp[x][path] >= dp[0][(1<<n) - 1]:
    #     return
    
    for i in range(1,n):
        if not mat[x][i]:
            continue
        if path&(1<<i):
            continue
        

        
        if dp[i][path|(1<<i)] > dp[x][path] + mat[x][i]:
            dp[i][path|(1<<i)] = dp[x][path] + mat[x][i]
            dfs(i,path|(1<<i))

for i in range(1,n):
    if mat[0][i]:
        path = 1|(1<<i)
        dp[i][path] = mat[0][i]
        dfs(i,path)
print(dp[0][(1<<n) - 1])