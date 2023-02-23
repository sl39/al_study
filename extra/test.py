TC = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for T in range(TC):
    m,n,k = map(int,input().split())
    mat = [[0]* m for i in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        mat[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                stack = [[i,j]]
                while stack:
                    x,y = stack.pop()
                    for dir in range(4):
                        nx = dx[dir] + x
                        ny = dy[dir] + y
                        if 0<= nx< n and 0<= ny < m and mat[nx][ny]:
                            mat[nx][ny] = 0
                            stack.append([nx,ny])
                cnt += 1
    print(cnt)