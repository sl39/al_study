# 아이디어
# 각각 성공할때마다 상하좌우에 각각의 가중치를 곱해서 dfs 를 한다
# 만약에 단순경로가 아닐 경우엔 백트레킹
# 끝까지 갈 경우에는 결과 값에 더해준다

arr = list(map(int,input().split()))
n = arr[0]
percent = arr[1:]
mat = [[0] * 30 for i in range(30)]

start = [15,15]
mat[15][15] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
mx = 0
def dfs(start,cnt,depth):
    global mx

    # 끝까지 잘 왔다면 결과 값에 더해줌
    if depth == n:
        mx += cnt
        return

    x,y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 안온 곳이라면 왔다고 방문 표시를 하고
        if not mat[nx][ny]:
            mat[nx][ny] = 1
            
            # 퍼센트를 곱해줌
            dfs((nx,ny),cnt * percent[i],depth+1)
            mat[nx][ny] = 0

dfs(start,1,0)

print(mx/(100**n))