from heapq import heappop,heappush

n,m,t,d = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(input().strip()))
def alpha(s):
    if s.isupper():
        ans  = ord(s) - ord("A")
    else:
        ans = ord(s) - ord("a") + 26
    return ans

start = (0,0)

visited = [[(1000000,1000000)] * m for i in range(n)]

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

q = []
heappush(q,(0,0,0,0))
while q:
    go, back, x,y = heappop(q)
    if visited[x][y][0] < go:
        continue
    if visited[x][y][0] == go and visited[x][y][1] < back:
        continue
    
    visited[x][y] = (go,back)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m and abs(alpha(mat[nx][ny])- alpha(mat[x][y])) <= t:
            a = alpha(mat[nx][ny])- alpha(mat[x][y])
            if a > 0:
                newgo = go + a**2
                newback = back + 1
            elif a == 0:
                newgo = go + 1
                newback = back + 1
            else:
                newgo = go + 1
                newback = back + a**2
            
            heappush(q, (min(newgo,go), min(newback,back),nx,ny))

for i in visited:
    print(i)