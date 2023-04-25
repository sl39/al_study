from collections import deque
import sys

input = sys.stdin.readline
TC = int(input())

for _ in range(TC):
    n,k = map(int,input().split())
    arr =[0] + list(map(int,input().split()))
    indegree = [0]*(n+1)
    graph =[[] for i in range(n+1)]
    for i in range(k):
        s,e = map(int,input().split())
        indegree[e] += 1
        graph[s].append(e)


    cost = [0]*(n+1)
    q = deque([])
    w = int(input())
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            cost[i] = arr[i]


    
    while q:
        node = q.popleft()
        for i in graph[node]:
            indegree[i] -= 1
            cost[i] = max(cost[i],cost[node] + arr[i])
            if indegree[i] == 0:
                q.append(i)


    print(cost[w])

