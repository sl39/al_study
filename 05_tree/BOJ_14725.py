alpha = [0]*26
R, C = map(int,input().split())
mat = []
for i in range(R):
    mat.append(list(input().strip()))


stack = [[0,0]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
alpha[ord(mat[0][0])- ord("A")] = 1
visited = [[0]*C for i in range(R)]
visited[0][0] = 1
while stack:
    x,y = stack.pop()
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<= nx < R and 0<= ny< C and not visited[nx][ny]:
            if not alpha[ord(mat[nx][ny]) - ord("A")]:
                alpha[ord(mat[nx][ny]) - ord("A")]= 1
                visited[nx][ny] = 1
                stack.append([nx,ny])
            else:
                if mat[x][y] != mat[nx][ny]:
                    visited[nx][ny] = 1
                    stack.append([nx,ny])


print(sum(alpha))
