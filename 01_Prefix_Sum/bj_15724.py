import sys
input = sys.stdin.readline
N, M = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
mys = [[0]*(M+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        mys[i][j] = mat[i-1][j-1] + mys[i-1][j] + mys[i][j-1] - mys[i-1][j-1]

K = int(input())
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    print(mys[x2][y2]+mys[x1-1][y1-1]-mys[x1-1][y2]-mys[x2][y1-1])
