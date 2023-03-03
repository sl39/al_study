n,m = map(int,input().split())

r,c,d = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

dic = {0: [0,-1],
       1: [1,0],
       2: [0,1],
       3: [-1,0]}

cnt = 0

def rotation(r,c,d):
    for i in range(1,4):
        nx = r + dic[(d-i)%4][0]
        ny = c + dic[(d-i)%4][1]
        if mat[nx][ny] == 0:
            return (nx,ny,(d-i)%4)
    return 0
cnt = 0
def check(r,c,d):
    global cnt
    while True:
        mat[r][c] = 2
        cnt += 1
        while mat[r+dic[d][0]][c+dic[d][1]] == 0:
            r = r+dic[d][0]
            c = c+dic[d][0]
            mat[r][c] = 2
            cnt += 1
        
        while not rotation(r,c,d):
            r = r - dic[d][0]
            c = c - dic[d][1]
        
        if rotation(r,c,d):
            r,c,d = rotation(r,c,d)
        else:
            return cnt

print(check(r,c,d))