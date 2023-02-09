# 앞의 숨바꼭질 문제와 비슷하게 푼다
# 여기서 문제는 2배를 순간이동 할 때는 시간이 걸리지 않는다는 것이다
# 그래서 처음에는 2*v를 맨 앞에 놓고, 2*v 일때는 앞이랑 동일한 횟수가 되게 하면 된다고 생각했다
# 90% 까지 왔을 때 실패 했는데 반례를 넣어 보니 1 17 일때는 1이 나와야 하는데 2 가 나왔다
# 보니깐 처음 시작할 때 즉 1 -> 2 로 갈때는 처음에 2*v 가 나와서 0 이 되지만
# 2 * v 를 하고 난 뒤에 v+1 을 한 값이 덮여씌어 지면서 개수가 하나씩 더 올라가게 된다
# 이걸 해결하기 위해 visited = [[0,0] for i in range(100001)]  이용해서 visted[v]에서 첫번째는 방문을 했는지 두번째는 얼마나 걸렸는지를 세기로 했다
# 그래서 만약에 처음 방문하면 v-1,v+1 이면 앞에서 +1 아니면 앞이랑 같이 이용하고
# 이미 방문 한 적이 있다면 그 전이랑 비교해서 v-1,v+1 이면 앞에서 +1 한것보다 작으면 바꾸고, 2*v 도 앞에 횟수랑 비교했을때 앞의 횟수가 작으면 바꾼다




from collections import deque
N, K = map(int,input().split())

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        ls = [2*v,v-1,v+1,]

        for i in range(3):
            if 0<= ls[i] < 100001 and not visited[ls[i]][0]:  # 방문 안했을 때
                if i == 0:
                    visited[ls[i]][1] = visited[v][1]
                    visited[ls[i]][0] = 1
                    q.append(ls[i])
                else:
                    visited[ls[i]][1] = visited[v][1] + 1
                    visited[ls[i]][0] = 1
                    q.append(ls[i])
            

            elif 0<= ls[i] < 100001 and visited[ls[i]][0]:          #이미 방문 한 곳일때 
                if i == 0:
                    if visited[ls[i]][1] > visited[v][1]:
                        visited[ls[i]][1] = visited[v][1]
                        q.append(ls[i])
                else:
                    if visited[ls[i]][1] > visited[v][1] + 1:
                        visited[ls[i]][1] = visited[v][1] + 1
                        q.append(ls[i])

                


visited = [[0,0] for i in range(100001)]
visited[N] = [1,0]
bfs(N)
print(visited[K][1])
