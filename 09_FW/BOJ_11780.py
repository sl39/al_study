n = int(input())
m = int(input())

graph = [[100000*n + 1]*n for i in range(n)]
visited = [[[i]for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        for k in range(n):
            if k==j or k == i:
                continue
            
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                visited[j][k] = visited[j][i] +  visited[i][k]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 100000*n + 1:
            graph[i][j] = 0

for i in graph:
    print(*i)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            print(0)
        else:
            print(len(visited[i][j])+1, end=" ")
            print(i+1, end=" ")
            for k in visited[i][j]:
                print(k+1, end=" ")
            print()