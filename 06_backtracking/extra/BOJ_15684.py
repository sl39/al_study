n,m,h = map(int,input().split())

mat = [[0]*(n+1) for i in range(h+2)]

for i in range(m):
    a,b = map(int,input().split())
    mat[a][b+1] = b
    mat[a][b] = b+1

ch = 0
def check():
    for x in range(h+1):
        for i in range(1,n+1):
            y = i
            if mat[x][y] != 0:
                y = mat[x][y]
        if y != i:
            return 0
    return 1

count = 4
def ladder(cnt,k):
    global count
    if cnt >=count:
        return

    if check():
        count = min(count,cnt)
        return
    if k == (n+1)*(h+1):
        return
    
    if k%(n+1) != 0 and k%(n+1) != n:
        if mat[k//(n+1)][k%(n+1)] == 0 and mat[k//(n+1)][(k+1)%(n+1)] == 0:
            mat[k//(n+1)][k%(n+1)] = (k + 1)%(n+1)
            mat[k//(n+1)][(k+1)%(n+1)] = k%(n+1)
            ladder(cnt+1,k+1)
            mat[k//(n+1)][k%(n+1)] = 0
            mat[k//(n+1)][(k+1)%(n+1)] = 0
    ladder(cnt,k+1)

ladder(0,0)
if count > 3:
    print(-1)
else:
    print(count)