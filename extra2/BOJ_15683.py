from copy import deepcopy


n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

arr = []
ans = 0
d = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(n):
    for j in range(m):
        if 1<=  mat[i][j] <= 5:
            arr.append((i,j))
        if mat[i][j]:
            ans += 1
ls = len(arr)
def dfs(mat,depth, cnt,ls,arr):
    global ans
    if depth == ls:
        ans = max(ans,cnt)

        return
    i,j = arr[depth]
    if mat[i][j] == 1:
        for i in d:
            matt = deepcopy(mat)
            dir = [i]
            matt,count = find(cnt,matt,dir,arr[depth])
            dfs(matt,depth+1, count,ls,arr)
    elif mat[i][j] == 2:
        dir = [d[0],d[2]]
        matt = deepcopy(mat)
        matt,count = find(cnt,matt,dir,arr[depth])
        dfs(matt,depth+1, count,ls,arr)
        matt = deepcopy(mat)
        dir = [d[1],d[3]]
        matt,count = find(cnt,matt,dir,arr[depth])
        dfs(matt,depth+1, count,ls,arr)

    elif mat[i][j] == 3:
        for i in range(4):
            matt = deepcopy(mat)
            dir = [d[i],d[(i+1)%4]]
            matt,count = find(cnt,matt,dir,arr[depth])
            dfs(matt,depth+1, count,ls,arr)

    elif mat[i][j] == 4:
        for i in range(4):
            matt = deepcopy(mat)
            dir = [d[i],d[(i+1)%4],d[(i+2)%4]]
            matt,count = find(cnt,matt,dir,arr[depth])
            dfs(matt,depth+1, count,ls,arr)

    else:
        dir = d
        matt = deepcopy(mat)
        matt,count = find(cnt,matt,dir,arr[depth])
        dfs(matt,depth+1, count,ls,arr)

def find(cnt,mat,dir,place):
    x,y =place
    for i in dir:
        dx,dy = i
        nx , ny = x,y
        while 0<= nx< n and 0<= ny < m:
            if 1<= mat[nx][ny] <= 5 or mat[nx][ny] == 7:
                nx += dx
                ny += dy
                continue
            if mat[nx][ny] == 6:
                break
            mat[nx][ny] = 7
            cnt += 1
            nx += dx
            ny += dy
    return (mat, cnt)

dfs(mat,0, ans,ls,arr)

print(n*m-ans)