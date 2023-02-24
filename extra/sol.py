import sys
sys.stdin = open("s_input.txt")

dx =[1,-1,0,0]
dy =[0,0,1,-1]

def bfs(start):
    stack = [start]
    cnt = 0
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and mat[nx][ny] -1 == mat[x][y]:
                cnt += 1
                stack.append([nx,ny])
    return cnt

TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    mat = []

    visited = [[0]*n for i in range(n)]
    for i in range(n):
        mat.append(list(map(int,input().split())))
    
    mx = 0 
    idx = mat[0][0]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = dx[k] +i
                ny = dy[k] +j
                if 0<= nx < n and 0<= ny < n:
                    if visited[nx][ny] and mat[i][j] == mat[nx][ny] +1:
                        visited[i][j] = visited[nx][ny] - 1
                        break
                    elif visited[nx][ny] and mat[i][j] == mat[nx][ny] -1:
                        visited[i][j] = visited[nx][ny] + 1
                        break
            else:
                visited[i][j] = bfs((i,j))
            if visited[i][j] > mx:
                mx = visited[i][j]
                idx = mat[i][j]
            elif visited[i][j] == mx and idx > mat[i][j]:
                idx = mat[i][j]
    print(f"#{T}",idx,mx+1)

                