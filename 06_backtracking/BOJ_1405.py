arr = list(map(int,input().split()))
n = arr[0]
percent = arr[1:]
mat = [[0] * 30 for i in range(30)]

start = [15,15]
mat[15][15] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
mx = 0
def dfs(start,cnt,depth):
    global mx
    if depth == n:
        mx += cnt
        return

    x,y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not mat[nx][ny]:
            mat[nx][ny] = 1
            dfs((nx,ny),cnt * percent[i],depth+1)
            mat[nx][ny] = 0

dfs(start,1,0)

print(mx/(100**n))