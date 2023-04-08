n,m = map(int,input().split())

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]



def s1(case):
    global arr
    d,s = case
    for i in arr:
        x,y = i
        x =x + s * dx[d]
        y =y + s * dy[d]
        visited[x%n][y%n] = 1
        mat[x%n][y%n] += 1
    arr = []

def s2():
    water= [] 
    for i in range(n):
        for j in range(n):
            cnt = 0
            if visited[i][j] == 1:
                for k in range(2,9,2):
                    x =i + dx[k]
                    y =j + dy[k]
                    if 0<= x < n and 0<= y < n and mat[x][y]:
                        cnt += 1
                water.append((i,j,cnt))
    for i in water:
        x,y,cnt = i
        mat[x][y] += cnt

def s3():
    for i in range(n):
        for j in range(n):
            if mat[i][j] >= 2 and not visited[i][j]:
                mat[i][j] -= 2
                arr.append((i,j))



mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))



magic = []
for i in range(m):
    magic.append(list(map(int,input().split())))

arr = [(n-1,0),(n-2,0),(n-1,1),(n-2,1)]

for i in magic:
    visited = [[0]*n for _ in range(n)]
    s1(i)

    s2()

    s3()


mys =0 
for i in mat:
    mys += sum(i)

print(mys)