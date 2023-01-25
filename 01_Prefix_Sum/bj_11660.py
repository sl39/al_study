import sys
input = sys.stdin.readline
N , M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(N)]
mys = [[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        mys[i][j] = mys[i-1][j] + mys[i][j-1] - mys[i-1][j-1] + mat[i-1][j-1]
for i in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    print(mys[x2][y2] - mys[x1-1][y2]- mys[x2][y1-1] +mys[x1-1][y1-1])