n = int(input())
coins = []

for i in range(n):
    coins.append(list(input().strip()))
rev_coins = [k[:] for k in coins]

for i in range(n):
    for j in range(n):
        if rev_coins[i][j] == "H":
            rev_coins[i][j] = 'T'
        else:
            rev_coins[i][j] == "H"

hm = n*n
for i in range(1<<n):
    arr = [0]*n
    test = 0
    for j in range(n):
        cnt = 0 
        if i&(1<<j):
            for k in range(n):
                if rev_coins[j][k] == 'H':
                    arr[k] += 1
            
        else:
            for k in range(n):
                if coins[j][k] == 'H':
                    arr[k] += 1
            
    print(arr)
    for i in arr:
        test += min(i,n-i)
    hm = min(test,hm)

print(hm)