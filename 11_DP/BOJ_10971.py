n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

mx = 1e9
visited = [0]*n
def dfs(start,depth,res,k):
    global mx
    if depth == n-1:
        if mat[start][k]:
            res += mat[start][k]
            mx = min(res,mx)
        return
    if mx <= res:
        return
    
    for i in range(n):
        if i!=k and visited[i] == 0 and mat[start][i]:
            visited[i] = 1
            dfs(i,depth+1,res+mat[start][i],k)
            visited[i] = 0
    
for start in range(n):
    dfs(start,0,0,start)
print(mx)