N,M = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
mys = [[0]*N for i in range(N)]
mys[0][0] = mat[0][0]
for i in range(0,N):
    for j in range(0,N):
        if j == 0:
            mys[i][j] = mat[i][j]
        else:
            mys[i][j] = mys[i][j-1] + mat[i][j]
for i in range(0,N):
    for j in range(0,N):
        if j == 0:
            mys[j][i] = mys[j][i]
        else:
            mys[j][i] = mys[j-1][i] + mat[j][i]
print(mys)