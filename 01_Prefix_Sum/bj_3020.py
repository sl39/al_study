N , M = map(int,input().split())
up = [0] * (M+1)
down = [0] * (M+1)

for i in range(N):
    A = int(input())
    if i %2 == 0:
        down[A] += 1
    else:
        up[A] += 1
up = up[1:]
down = down[1:]
for i in range(M-2,0-1,-1):
    down[i] = down[i+1] + down[i]
    up[i] = up[i+1] + up[i]
cnt = 1
mys = N
for i in range(M):
    if mys == down[i] + up[M-i-1]:
        cnt += 1
    elif mys > down[i] + up[M-i-1]:
        mys = down[i] + up[M-i-1]
        cnt = 1
print(mys,cnt)