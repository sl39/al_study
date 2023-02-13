import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    K = int(input())
    ls = list(map(int,input().split()))
    ls_sum = sum(ls) + 2
    files = [0] *ls_sum
    cost = [0] * ls_sum

    for i in ls:
        files[i] += 1
    i = 0
    while K > 1:
        i += 1
        if files[i]:
            if files[i] % 2:
                files[i*2] += files[i]//2
                cost[i*2] += files[i]//2
                K -= files[i]//2
                files[i] = 1
                for j in range(i+1,ls_sum):
                    if files[j]:
                        files[j+i] += 1
                        cost[j+i] += 1
                        files[j] -= 1
                        files[i] -= 1
                        K -= 1
                        break
            else:
                files[i*2] += files[i]//2
                cost[i*2] += files[i]//2
                K -= files[i]//2
                files[i] = 0
    mys = 0
    for i in range(ls_sum):
        if cost[i]:
            mys += cost[i] * i
    print(mys)

