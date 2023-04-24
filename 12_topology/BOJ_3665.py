from collections import deque

TC = int(input())
for _ in range(TC):
    n = int(input())
    arr = [0]+list(map(int,input().split()))
    m = int(input())
    graph = [[0]*(n+1) for i in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            graph[arr[j]][arr[i]] = 1
            indegree[arr[j]] += 1

    
    

    for i in range(m):
        s,e = map(int,input().split())
        if graph[s][e]:
            graph[s][e] = 0
            graph[e][s] = 1
            if indegree[s]:
                indegree[s] -= 1
            indegree[e] += 1
        else:
            graph[e][s] = 0
            graph[s][e] = 1
            if indegree[e]:
                indegree[e] -= 1
            indegree[s] += 1

    
    arr = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            arr.append(i)
            break
    
    q = deque(arr)
    while q:
        node = q.popleft()
        for i in range(1,n+1):
            if graph[i][node]:
                graph[i][node] = 0
                indegree[i] -= 1
                if indegree[i] == 0:
                    arr.append(i)
                    q.append(i)
    
    if len(arr) == n:
        print(*arr)
    else:
        print('IMPOSSIBLE')
    

