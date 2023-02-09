from collections import deque
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        for i in [v-1,v+1,2*v]:
            
            if 0<= i < 100001:
                if not visited[i][0]:
                    visited[i][1] = visited[v][1] + 1
                    visited[i][0] = visited[v][0]
                    q.append(i)
                elif visited[i][1] == visited[v][1] + 1:
                    visited[i][0] += visited[v][0]

    


N, K = map(int,input().split())
visited = [[0,0] for _ in range(100001)]
visited[N] = [1,0]
bfs(N)
print(visited[K][1])
print(visited[K][0])
