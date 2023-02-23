import sys
sys.stdin = open("s_input.txt")


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(start, m):
    global cnt
    x,y = start
    for k in range(4):
        nx = dx[k] +x
        ny = dy[k] +y
        if 0<= nx < n and 0<= ny <n:
            if mat[x][y] +1 == mat[nx][ny]:
                dfs([nx,ny], m+1)
            else:
                if m > cnt[1]:
                    cnt = [[i,j],m]
                elif m == cnt[1] and mat[i][j] < mat[cnt[0][0]][cnt[0][1]]:
                    cnt = [[i,j],m]




TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    cnt = [[0,0],0]
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            dfs([i,j], 0)
    print(f"#{T}",mat[cnt[0][0]][cnt[0][1]],cnt[1]+1)