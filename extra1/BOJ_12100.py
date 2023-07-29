n = int(input())
mat = []
for  i in range(n):
    mat.append(list(map(int,input().split())))

ans = 0

# 0은 왼쪽 1은 오른쪽 2는 위쪽 3은 아래쪽
def moveto(k,ls,depth):
    global ans
    cnt = 0
    for i in ls[3]:
        cnt = max(cnt, max(i))
    if cnt *(2**(5-depth)) <= ans:
        return

    if depth == 5:
        mx = 0
        for i in range(n):
            for j in range(n):
                mx = max(mx,ls[3][i][j])
        ans = max(mx,ans)
        return


    if k == 0:
        visited = [[0]*n for i in range(n)]
        for i in range(n):
            start = 0
            val = ls[3][i][0]
            for j in range(1,n):
                if ls[3][i][j] == 0:
                    continue
                if val == 0:
                    if ls[3][i][j] != 0:
                        val = ls[3][i][j]
                else:
                    if val == ls[3][i][j]:
                        visited[i][start] = 2*val
                        val = 0
                        start += 1
                    else:
                        visited[i][start] = val
                        val = ls[3][i][j]
                        start += 1
            visited[i][start] = val
        if visited == ls[1] or visited == ls[0] or visited == ls[2] or visited == ls[3]:
            mx = 0
            for i in visited:
                mx = max(max(i),mx)
            ans = max(mx,ans)
            return
        ls = [ls[1],ls[2],ls[3],visited]
        for i in range(4):
            moveto(i,ls,depth+1)


    elif k == 1:
        visited = [[0]*n for i in range(n)]
        for i in range(n):
            start = n-1
            val = ls[3][i][n-1]
            for j in range(n-2,-1,-1):
                if ls[3][i][j] == 0:
                    continue
                if val == 0:
                    if ls[3][i][j] != 0:
                        val = ls[3][i][j]
                else:
                    if val == ls[3][i][j]:
                        visited[i][start] = 2*val
                        val = 0
                        start -= 1
                    else:
                        visited[i][start] = val
                        val = ls[3][i][j]
                        start -= 1

            visited[i][start] = val
        if visited == ls[1] or visited == ls[0] or visited == ls[2] or visited == ls[3]:
            mx = 0
            for i in visited:
                mx = max(max(i),mx)
            ans = max(mx,ans)
            return
        ls = [ls[1],ls[2],ls[3],visited]
        for i in range(4):
            moveto(i,ls,depth+1)
    
    elif k == 2:
        visited = [[0]*n for i in range(n)]
        for i in range(n):

            start = 0
            val = ls[3][0][i]
            for j in range(1,n):
                if ls[3][j][i]== 0:
                    continue
                if val == 0:
                    if ls[3][j][i] != 0:
                        val = ls[3][j][i]
                else:
                    if val == ls[3][j][i]:
                        visited[start][i] = 2*val
                        val = 0
                        start += 1
                    else:
                        visited[start][i] = val
                        val = ls[3][j][i]
                        start += 1

            visited[start][i] = val
        if visited == ls[1] or visited == ls[0] or visited == ls[2] or visited == ls[3]:
            mx = 0
            for i in visited:
                mx = max(max(i),mx)
            ans = max(mx,ans)
            return
        ls = [ls[1],ls[2],ls[3],visited]
        for i in range(4):
            moveto(i,ls,depth+1)


    elif k == 3:
        visited = [[0]*n for i in range(n)]
        for i in range(n):
            start = n-1
            val = ls[3][n-1][i]
            for j in range(n-2,-1,-1):
                if ls[3][j][i] == 0:
                    continue
                if val == 0:
                    if ls[3][j][i] != 0:
                        val = ls[3][j][i]
                else:
                    if val == ls[3][j][i]:
                        visited[start][i] = 2*val
                        val = 0
                        start -= 1
                    else:
                        visited[start][i] = val
                        val = ls[3][j][i]
                        start -= 1

            visited[start][i] = val
        if visited == ls[1] or visited == ls[0] or visited == ls[2] or visited == ls[3]:
            mx = 0

            for i in visited:
                mx = max(max(i),mx)
            ans = max(mx,ans)
            return
        ls = [ls[1],ls[2],ls[3],visited]
        for i in range(4):
            moveto(i,ls,depth+1)



visited = [[0]*n for i in range(n)]
for i in range(4):
    moveto(i,[visited,visited,visited,mat],0)

print(ans)

