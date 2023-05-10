from heapq import heappop,heappush,heapify

TC = int(input())
for _ in range(TC):
    n = int(input())
    arr = list(map(int,input().split()))
    heapify(arr)
    ans = 0
    while n> 1:
        a = heappop(arr)
        b = heappop(arr)
        ans += a+b
        heappush(arr,a+b)
        n -= 1
    print(ans)