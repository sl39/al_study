n,m,h = map(int,input().split())

mat = [[0]*n for i in range(h+1)]

for i in range(m):
    a,b = map(int,input().split())
    mat[a-1][b-1] = 1



def path():
    for i in range(n):
        start = i
        for j in range(h):
            if mat[j][start] == 1:
                start += 1
            elif start-1 >=0 and mat[j][start-1] == 1:
                start -= 1
        if start != i:
            return 0
    return 1


result = 4
def dfs(t,cnt):
    global result
    if cnt >= result:
        return

    if path():
        result = min(result,cnt)
        return


    for i in range(t, can-1):
        x,y = candy[i]
        if y == 0:
            if mat[x][y+1] == 0:
                mat[x][y] = 1
                dfs(i+1, cnt + 1)
                mat[x][y] = 0

        elif mat[x][y-1] == 0 and mat[x][y+1] == 0:
            mat[x][y] = 1
            dfs(i+1,cnt+1)
            mat[x][y] = 0


candy = []


for j in range(h+1):
    for i in range(n-1):
        if mat[j][i] == 0:
            candy.append(((j,i)))

can = len(candy)


dfs(0,0)
if result >3:
    print(-1)
else:
    print(result)