n = int(input())

m = int(input())

graph = [[n*100000+1]*n for i in range(n)]


for i in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)
    
for i in range(n):
    for j in range(n):
        if j==i:
            continue
        for k in range(n):
            if j == k or k== i:
                continue
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]



for i in graph:
    for j in range(n):
        if i[j] == n*100000+1:
            i[j] = 0
    
    print(*i)