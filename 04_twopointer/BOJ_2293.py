## 어떤 위치의 개수는 코인만큼 뺀 위치를 계속해서 더해주는 것


n, k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()
c = max(coins)
step = [0] * (k+1+c)
step[0] = 1
for j in coins:
    for i in range(0,k+1):
        step[i+j] += step[i]
print(step[k])

