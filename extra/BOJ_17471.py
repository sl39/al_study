from collections import deque


n = int(input())
population = [0] + list(map(int,input().split()))
ppp =sum(population)
graph = [[] for i in range(n+1) ]

cnt = 0
for i in range(1,n+1):
    p, *nodes = map(int,input().split())
    for j in nodes:
        graph[i].append(j)
visited = [0] * (n+1)

def vote():
    if n == 2:
        return abs(population[2]- population[1])
    cot = 0
    for i in range(1,n+1):
        if not graph[i]:
            cot += 1
        if cot > 2 and n >2:
            return -1
    
    if cot == 1:
        for i in range(1,n+1):
            if not graph[i]:
                return abs(ppp- 2* population[i])
    
    com(2,[1])


mini = 1000
def com(i,res):
    visited[i] = 1
    q = deque([1])
    while q:
        x = q.popleft()
        


    if i == n+1:
        return
    
    com(i+1,res+[i])
    visited[i] = 0
    com(i+1,res)