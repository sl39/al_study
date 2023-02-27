n = int(input())


d = [9,9*8,9*8*7,9*8*7*6,9*8*7*6*5,9*8*7*6*5*4]

for i in range(5):
    d[i+1] = d[i] + d[i+1]

res = 0
cnt = 0
result = ""
chosen = [0] * 10
def per(depth,res):
    global cnt, result
    if depth == idx + 2:
        cnt += 1
        if cnt == n:
            for i in res:
                result += str(i)
        return

    if cnt == n:
        return

    for i in range(10):
        if depth == 0:
            chosen[i] = 1
            per(depth+1, res+[i])
            chosen[i] = 0
        else:
            if not chosen[i] and  res[-1] > i :
                chosen[i] = 1
                per(depth + 1, res + [i])
                per(depth, res)
                chosen[i] = 0



if n < 10:
    print(n)
elif d[-1] < n:
    print(-1)
else:
    for i in range(6):
        if n > d[i]:
            idx = i
    n = n - d[idx]-1

    per(0,[])
    print(result)