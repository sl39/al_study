n = int(input())

dp = [[[0]*1024 for i in range(10)] for j in range(n+1)]

for i in range(1,10):
    dp[1][i][1<<i] = 1

for length in range(1,n):
    for last in range(10):
        for bit in range(1024):
            if last < 9:
                nextbit = bit|(1<<(last+1))
                dp[length+1][last+1][nextbit] += dp[length][last][bit]%1000000000
            if last > 0:
                nextbit = bit|(1<<(last-1))
                dp[length+1][last-1][nextbit] += dp[length][last][bit]%1000000000

answer = 0
for last in range(10):
    answer += dp[n][last][1023]

print(answer%1000000000)