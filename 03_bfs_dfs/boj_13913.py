# 기존하고 같은데 다만 경로를 추가 해야 되기 때문에
# 각 칸에 길이가 2인 리스트를 만들어서
# 앞에는 이때까지 얼마나 했는지를
# 뒤에는 걸처온 경로를 저장한다
# 그리고 메모리 초과를 해결하기 위해서 
# v-1, v+1, 2*v 의 작업이 끝나면
# visited[v][1]을 0으로 재정의 해줘서
# 메모리의 부담감을 줄여줌
# 그리고 N > K 이면
# 시간은 N-K 이고
# 경로는 N 부터 K 까지 하나씩 줄여 나가준다


from collections import deque
import sys
input = sys.stdin.readline
N , K = map(int,input().split())

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            return visited[K]
        for i in [v-1,v+1,2*v]:
            if 0<= i < 100001 and not visited[i][0]:
                visited[i][0] = visited[v][0] + 1
                visited[i][1] = visited[v][1][:]
                visited[i][1].append(i)
                q.append(i)
        visited[v][1] = 0
            


visited = [[0,[]] for _ in range(100001)]
visited[N] = [0,[N]]
if N > K:                                   # N>K 일때
    print(N-K)
    print(*list(range(N,K-1,-1)))
else:                                       # 아니면 bfs 함수 실행
    res = bfs(N)
    print(res[0])
    print(*res[1])
