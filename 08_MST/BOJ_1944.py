# prim을 이용해서 해결
# heapq 를 이용함
# K에 도착했을 때 로봇을 복제해서 보내면 되므로
# q에다가 (0,(좌표))를 넣음
# 그리고 이전에 이동한 거리를 res 에다가 넣어줌
# 아니면 이전 이동 거리에 +1 (c,(좌표))를 넣음
# 이미 방문한 k라면 k위치의 mat 값을 1로 넣어줌
# res의 길이와 열쇠의 개수가 같으면
# res의 합을 출력
# 아니면 -1을 출력


from heapq import heappop,heappush
n,m = map(int,input().split())

mat =[]
for i in range(n):
    mat.append(list(input().strip()))
visited = [[n*n +1]*n for i in range(n)]


for i in range(n):
    for j in range(n):
        if mat[i][j] == "S":
            start = (0,i,j)

q = []
heappush(q,start)

dx = [0,0,-1,1]
dy = [1,-1,0,0]
res = []
while q:
    c,x,y = heappop(q)
    if c >= visited[x][y]:
        continue
    visited[x][y] = c
    t = 0
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        # 상하좌우에
        if 0<= nx < n and 0<= ny < n:
            
            # 만약에 0 이면 지금까지 이동 거리에 +1 을 해주고 heappush
            if mat[nx][ny] == "0":
                heappush(q,(c+1,nx,ny))
                
            # 만약 K라면 (0,(좌표))를 heappush
            elif mat[nx][ny] == "K" and visited[nx][ny] == n*n+1:
                heappush(q,(0,nx,ny))
                mat[nx][ny] = 1
                
                
                
                # 5 3
                # 11111
                # 1S1K1
                # 10001
                # 1K1K1
                # 11111
                # 이 케이스를 해결하기 위해 
                if c>1:
                    t += 1
                    
                else:
                    # c=0 일때
                    # 즉 K가 연속적으로 연결되어 있을 때
                    res.append(c+1)
                    
    # 바로 위 케이스를 해결 하기 위해
    # 상하좌우에 K가 2개 이상 있다면
    # 한곳을 방문 하고 나머지를 그 자리에서 다시 시작하면 되므로
    if t > 1:
        for i in range(t-1):
            res.append(2)
        res.append(c+1)
    elif t== 1:
        res.append(c+1)



if len(res) != m:
    print(-1)
else:
    print(sum(res))


# 5 3
# 11111
# 1S1K1
# 10001
# 1K1K1
# 11111
