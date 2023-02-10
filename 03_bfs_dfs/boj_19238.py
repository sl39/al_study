from collections import deque
import sys
import copy
input = sys.stdin.readline
N , P , gas = map(int,input().split())


def check(start ,end):
    new_mat = copy.deepcopy(mat)
    q = deque([start])
    while q:
        v = q.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0<= nx < N and 0<= ny < N and new_mat[nx][ny] != -1 and new_mat[nx][ny] != 1:
                new_mat[nx][ny] = -1
                q.append([nx,ny])
            if [nx,ny] == end:
                return 1
    return 0
                



def fpassengers(cap):                                    # 택시랑 가장 가까운 승객 찾음
    global mat, f
    if cap[2] == -1:
        return [-1,-1,-1,-1]
    q = deque([cap])
    while q and gas:
        v = q.popleft()
        if v[2] < max(f):
            pass
        else:
            if mat[v[0]][v[1]] in ls:
                result = [v[0], v[1] , v[2], mat[v[0]][v[1]]]
                mat[v[0]][v[1]] = 0
                f.append(v[2])
                results.append(result)
            for i in range(4):
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]
                if 0<= nx < N and 0<= ny < N and mat[nx][ny] != 1:
                    q.append([nx,ny,v[2]-1])


def fdestination(cap):                                    # 목적지
    global mat
    if cap[2] == -1:
        return [-1,-1,-1]
    q = deque([cap])
    destination = cap[3] + P
    while q and gas:
        v = q.popleft()
        if v[2] == -1:
            return [-1,-1,-1]
        if mat[v[0]][v[1]] ==  destination:
            mat[v[0]][v[1]] = 0
            return [v[0], v[1] , v[2] + 2 * (cap[2] - v[2])]
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0<= nx < N and 0<= ny < N and mat[nx][ny] != 1:
                q.append([nx,ny,v[2]-1])

def fcap(results):
    global mat
    caps = results[0]
    t = 0
    for i in range(len(results)):
        if results[i][0] < caps[0]:
            caps = results[i]
            t = i
        elif results[i][0] == caps[0]:
            if results[i][1] < caps[1]:
                caps = results[i]
                t = i
    for i in range(len(results)):
        if i == t:
            pass
        else:
            mat[results[i][0]][results[i][1]] = results[i][3]
    
    return caps





mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))

x, y = map(int,input().split())
cap = [x-1,y-1,gas]
passengers = []
for i in range(2,P+2):
    x1,y1,x2,y2, = map(int,input().split())
    passengers.append([x1-1,y1-1,x2-1,y2-1])
    mat[x1-1][y1-1] = i
    mat[x2-1][y2-1] = i + P
ls = list(range(2,P+2))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
for i in passengers:
    if check(i[0:2] ,i[2:4]):
        cnt += 1
for i in passengers:
    if check(i[0:2],cap):
        cnt += 1
        



if cnt == 2*P:
    path = 0
    while path < P:
        if cap[2] == -1:
            break
        f = [-1]
        results = []
        fpassengers(cap)
        cap = fcap(results)
        if cap[2] == -1:
            break
        cap = fdestination(cap)
        path += 1

    print(cap[2])
else:
    print(-1)