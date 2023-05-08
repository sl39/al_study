n = int(input())
m = int(input())

visited1 = [[n+1]*n for i in range(n)]
visited2 = [[n+1]*n for i in range(n)]
for i in range(m):
    s,e = map(int,input().split())
    visited1[e-1][s-1] = 1
    visited2[s-1][e-1] = 1


for i in range(n):
    for j in range(n):
        for k in range(n):
            visited1[j][k] = min(visited1[j][i]+ visited1[i][k], visited1[j][k])

            visited2[j][k] = min(visited2[j][i]+ visited2[i][k], visited2[j][k])
            
for i in range(n):
    res = -1
    for j in range(n):
        if (visited1[i][j] == n+1 and visited2[i][j] == n+1):
            res += 1
    print(res)