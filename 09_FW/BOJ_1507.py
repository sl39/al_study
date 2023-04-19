n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
visited = [[1]*n for i in range(n)]
flag = 1
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i ==k or k == j:
                continue
            if mat[j][k] == mat[j][i] + mat[i][k]:
                visited[j][k] = 0
            elif mat[j][k] > mat[j][i] + mat[i][k]:
                flag = 0



if flag:
    nys = 0
    for i in range(n):
        for j in range(i,n):
            if visited[i][j]:
                nys += mat[i][j]
    print(nys)
else:
    print(-1)