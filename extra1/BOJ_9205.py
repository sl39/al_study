from collections import deque

Tc = int(input())

def bfs(start):
    q = deque([start])
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                if i == n+1:
                    return 1
                visited[i] = 1
                q.append(i)
    return 0



for _ in range(Tc):
    n = int(input())
    arr = []
    for i in range(n+2):
        arr.append(list(map(int,input().split())))
    visited = [0]*(n+2)
    visited[0] = 1
    graph =[[] for i in range(n+2)]
    for i in range(n+1):
        for j in range(1,n+2):
            res = abs(arr[i][0]-arr[j][0]) + abs(arr[i][1]-arr[j][1])
            if res <= 1000:
                graph[i].append(j)
                graph[j].append(i)

    ans  = 0
    
    if bfs(0):
        print('happy')
    else:
        print('sad')
