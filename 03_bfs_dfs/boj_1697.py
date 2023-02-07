N, K = map(int,input().split())

res = K-N
cnt = 0

def Bfs(num1 , num2,cnt):
    global res
    if cnt >= res:
        return

    if num2 == num1:
        if res > cnt:
            res = cnt
        return

    if num2 > num1:
        if num2%2 == 0:
            if abs(num2//2 - num1) < abs(num2 - num1):
                Bfs(num1 , num2//2,cnt+1)

            else:
                if res > cnt + num2 - num1:
                    res = cnt + num2 - num1 
                    return
        else:

            if abs((num2-1)//2 - num1) < abs((num2+1)//2 - num1):
                Bfs(num1,(num2-1)//2,cnt+2)

            else:
                Bfs(num1,(num2+1)//2,cnt+2)
    else:
        if res > cnt + num1 - num2:
            res = cnt + num1 - num2
        return




if N > K:
    print(N-K)
elif N == K:
    print(0)
else:
    Bfs(N,K,0)
    print(res)