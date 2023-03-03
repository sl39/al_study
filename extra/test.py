N, K = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0] * (N+1)

# 첫 항 만들기
# S1 = S0 + A0~A4
for k in range(K):
    sum[1] += arr[k]

# 누적합
# S2 = S1 + A5 - A0
# S3 = S2 + A6 - A1
for i in range(2, N-K+2):
    sum[i] = sum[i-1] + arr[i-2+K] - arr[i-2]
print(max(sum[1:]))