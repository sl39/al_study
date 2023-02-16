n, k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()
c = max(coins)
step = [0] * (k+1+c)
for i in coins:
    step[i] += 1
for i in range(1,k+1):
    if step[i]:
        for j in coins:
            step[i+j] += step[i]
print(step)

