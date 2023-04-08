r,c,t =map(int,input().split())
mat = []
for i in range(r):
    mat.append(list(map(int,input().split())))

start = []
for i in range(r):
    for j in range(c):
        if mat[i][j] == -1:
            start.append(i)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def spread():
    arr = []
    for i in range(r):
        for j in range(c):
            if mat[i][j] != 0 and mat[i][j] != -1:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0<= nx < r and 0<= ny < c and mat[nx][ny] != -1:
                        cnt += 1
                        arr.append((nx,ny,mat[i][j]//5))
                    
                mat[i][j] -= (mat[i][j]//5) * cnt
    
    for i in arr:
        x,y,count = i
        mat[x][y] += count
    return

def rotationup():
    up = start[0]

    now = mat[up][1]
    mat[up][1]= 0
    for i in range(2,c):
        next = mat[up][i]
        mat[up][i] = now
        now = next
    
    for i in range(up-1,-1,-1):
        next = mat[i][c-1]
        mat[i][c-1] = now
        now = next
    
    for i in range(c-2,-1,-1):
        next = mat[0][i]
        mat[0][i] = now
        now = next
    
    for i in range(1,up):
        next = mat[i][0]
        mat[i][0] = now
        now = next

def rotationdown():
    down = start[1]

    now = mat[down][1]
    mat[down][1]= 0
    for i in range(2,c):
        next = mat[down][i]
        mat[down][i] = now
        now = next
    
    for i in range(down+1,r):
        next = mat[i][c-1]
        mat[i][c-1] = now
        now = next
    
    for i in range(c-2,-1,-1):
        next = mat[r-1][i]
        mat[r-1][i] = now
        now = next
    
    for i in range(r-2,down,-1):
        next = mat[i][0]
        mat[i][0] = now
        now = next

while t >0:
    spread()
    rotationup()
    rotationdown()
    t -= 1

mys = 2
for i in mat:
    mys += sum(i)

print(mys)