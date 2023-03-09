n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
k = max(arr) + 1

if k== 2:
    dp= [0,1]
elif k==3:
    dp=[0,1,2]
elif k==4:
    dp=[0,1,2,3]
else:
    dp = [1]*(k+3)
    for i in range(2,k+2):
        dp[i] += dp[i-2]
    
    for i in range(3,k+2):
        dp[i] += dp[i-3]
    
for i in arr:
    print(dp[i])


