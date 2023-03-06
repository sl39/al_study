n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
visited = [0] * 9
visited[0] = 1
lineup = [0] *9
lineup [3] = 0
result = 0
def perm(depth):
    global result
    if depth == 9:
        A = score()
        result = max(A,result)
        return
    if depth == 3:
        perm(depth+1)
    else:
        for i in range(9):
            if not visited[i]:
                visited[i] = 1
                lineup[depth] = i
                perm(depth+1)
                visited[i] = 0
                lineup[depth] = 0


def score():
    point = 0
    inning = 0
    out = 0
    batter = 0
    b1 =0
    b2 =0
    b3 =0
    while inning < n:
        if mat[inning][lineup[batter]] == 0:
            out += 1
        elif mat[inning][lineup[batter]] == 1:
            if b3:
                point += 1
            b3 =b2
            b2 =b1
            b1 =1
        elif mat[inning][lineup[batter]] == 2:
            if b3:
                point += 1
            if b2:
                point += 1
            b3 = b1
            b2 = 1
            b1 = 0
        elif mat[inning][lineup[batter]] == 3:
            if b3:
                point += 1
            if b2:
                point += 1
            if b1:
                point += 1
            b1,b2 = 0,0
            b3 =1
        
        else:
            point += b1 + b2 + b3 +1
            b1,b2,b3 = 0,0,0
        

        if out == 3:
            out = 0
            b1, b2, b3 = 0,0,0
            inning += 1
        batter = (batter + 1)%9
    return point


perm(0)
print(result)