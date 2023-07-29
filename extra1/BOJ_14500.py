from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
cases = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(1,1),(0,2)]]
rotations =[
    (0,1),
    (-1,0)
]
n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

def rot(a,b):
    global answer
    for i in cases:
        res = 0
        for j in i:
            x,y = j
            if 0<= a+x < n and 0<= b+y < m:
                res += mat[a+x][b+y]
            else:
                break
        else:
            answer = max(res,answer)
        res = 0
        for j in i:
            y,x = j
            if 0<= a+x < n and 0<= b+y < m:
                res += mat[a+x][b+y]
            else:
                break
        else:
            answer = max(res,answer)
    for i in range(1,4):
        for j in cases:
            res = mat[a][b]
            res1 = mat[a][b]
            for t in range(1,4):
                x,y = j[t]
                cnt = 1
                cnt1 = 1
                for l in range(i):
      
                    x,y = x*rotations[0][0] + y*rotations[0][1],x*rotations[1][0] + y*rotations[1][1]
                if 0<= a+x < n and 0<= b+y < m:
                    cnt += 1
                    res += mat[a+x][b+y]
                if 0<= a+y < n and 0<= b+x < m:
                    cnt1 += 1
                    res1 += mat[a+y][b+x]
            if cnt == 4:
                answer = max(res,answer)
            if cnt1 == 4:
                answer = max(res1,answer)

# for i in range(n):
#     for j in range(m):
#         rot(i,j)
rot(3,0)
print(answer)



