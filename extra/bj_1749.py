N,M = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
mys = [[0]*(M+1) for i in range(N+1)]
mini = 200*200 *10000
maxi = (-200)*200*10000

for i in range(1,N+1):
    for j in range(1,M+1):
        mys[i][j] = -mys[i-1][j-1] + mys[i-1][j] + mys[i][j-1] + mat[i-1][j-1]