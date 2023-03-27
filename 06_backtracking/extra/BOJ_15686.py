n,m = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

BBQ = []
house = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            BBQ.append((i,j))
        if mat[i][j] == 1:
            house.append((i,j))


cs = len(BBQ)
mx = 13*2500


def com(i,depth, res):
    global mx
    if depth == m:
        mx = min(mx,distance(res))
        return
    if i == cs:
        return
    com(i+1,depth+1, res + [BBQ[i]])
    com(i+1,depth,res)



def distance(res):
    ans = 0
    for i in house:
        nn = n*n
        x,y = i
        for j in res:
            nx,ny = j
            a = abs(x-nx) + abs(y-ny)
            nn = min(a,nn)
        ans += nn
        if ans > mx:
            return 13*2500
    return ans

com(0,0,[])

print(mx)