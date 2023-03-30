n,k = map(int,input().split())

graph = [[0]*n for i in range(n)]

for i in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
m = int(input())


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or k == j:
                continue
            
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in range(m):
    a,b = map(int,input().split())
    if graph[a-1][b-1]:
        print(-1)
    elif graph[b-1][a-1]:
        print(1)
    else:
        print(0)
