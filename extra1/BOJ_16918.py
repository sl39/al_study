r,c,n = map(int,input().split())
mat = []
for i in range(r):
    mat.append(list(input().strip()))

pung = [[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        if mat[i][j] == "O":
            pung[i][j] = 2

dx= [0,0,-1,1]
dy = [1,-1,0,0]



t = 1
while t < n:

    arr = []
    for i in range(r):
        for j in range(c):
            if pung[i][j]:
                pung[i][j] -= 1
            else:
                pung[i][j] = 3
            if pung[i][j] == 0:
                arr.append((i,j))
    
    for x in arr:
        i,j = x
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<= nx < r and 0<= ny <c:
                pung[nx][ny] = 0
    t += 1

for i in range(r):
    for j in range(c):
        if pung[i][j]:
            print('O', end='')
        else:
            print('.', end="")
    print()