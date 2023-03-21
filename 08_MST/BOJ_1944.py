from heapq import heappop,heappush
n,m = map(int,input().split())

mat =[]
for i in range(n):
    mat.append(list(input().strip()))
visited = [[n*n +1]*n for i in range(n)]


for i in range(n):
    for j in range(n):
        if mat[i][j] == "S":
            start = (0,i,j)

q = []
heappush(q,start)

dx = [0,0,-1,1]
dy = [1,-1,0,0]
res = []
while q:
    c,x,y = heappop(q)
    if c >= visited[x][y]:
        continue
    visited[x][y] = c
    t = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx < n and 0<= ny < n:
            if mat[nx][ny] == "0":

                heappush(q,(c+1,nx,ny))
            elif mat[nx][ny] == "K" and visited[nx][ny] == n*n+1:
                heappush(q,(0,nx,ny))
                # visited[nx][ny] = c
                mat[nx][ny] = 1
                if c>1:
                    t += 1
                else:
                    res.append(c+1)
    if t > 1:
        for i in range(t-1):
            res.append(2)
        res.append(c+1)
    elif t== 1:
        res.append(c+1)



if len(res) != m:
    print(-1)
else:
    print(sum(res))


# 5 3
# 11111
# 1S1K1
# 10001
# 1K1K1
# 11111
