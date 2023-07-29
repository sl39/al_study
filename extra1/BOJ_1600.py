from collections import deque
t = int(input())
w,h = map(int,input().split())
if w == h == 1:
    print(0)
    exit()
mat = []
for i in range(h):
    mat.append(list(map(int,input().split())))
if mat[-1][-1] == 1:
    print(-1)
    exit()
visited = [[w*h + 1]*w for i in range(h)]
visited[0][0] = 0
move = [(2,1),(1,2),(-2,1),(1,-2),(2,-1),(-1,2),(-2,-1),(-1,-2)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    for i in dxy:
        nx =i[0] + x
        ny =i[1] + y
        if 0<= nx < h and 0<= ny < w and visited[nx][ny] == w*h + 1 and not mat[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))

cnt = 0
while cnt < t:
    cnt += 1
    q = deque([])
    visited1 = [[0] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if mat[i][j] or visited1[i][j]:
                continue
            for k in move:
                dx,dy = k
                nx = dx + i
                ny = dy + j
                if 0<= nx < h and 0<= ny < w and  mat[nx][ny] == 0 and visited[i][j] + 1 < visited[nx][ny] and visited1[nx][ny] == 0:
                    visited[nx][ny] = visited[i][j] + 1
                    visited1[nx][ny] = 1
                    q.append((nx,ny))
    while q:
        x,y = q.popleft()
        for i in dxy:
            nx =i[0] + x
            ny =i[1] + y
            if 0<= nx < h and 0<= ny < w and not mat[nx][ny]:
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
if visited[-1][-1] == w*h + 1:
    print(-1)
else:
    print(visited[-1][-1])



