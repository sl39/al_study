N, K = map(int,input().split())
div = 1000000000

arr = [0]* (N+K+1)
arr[0] = 1
arr[1] = 1
for i in range(2,N+K+1):
    arr[i] = arr[i-1] * i



print((arr[N+K-1]//(arr[N]*arr[K-1]))%div)

