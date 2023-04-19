n = int(input())
for i in range(n):
    k = int(input())
    coins = list(map(int,input().split()))
    target = int(input())
    mat = [[0] * (target+1) for i in range(k)]
    for j in range(k):
        mat[j][0] = 1
    for p in range(k):
        coin = coins[p]
        
        for q in range(1,target+1):
            if coin > q:
                mat[p][q] = mat[p-1][q]
            else:

                mat[p][q] = mat[p][q-coin]+mat[p-1][q]

    print(mat[-1][target])

            