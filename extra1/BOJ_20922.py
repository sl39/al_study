n,k = map(int,input().split())
arr = list(map(int,input().split()))

nums = [0] * 100001
start = 0
end = 0
nums[arr[0]] = 1

ans = 0
for end in range(1,n):
    nums[arr[end]] += 1
    
    while nums[arr[end]] > k:
        nums[arr[start]] -= 1
        start += 1
    ans = max(ans,end-start+1)
print(ans)