from heapq import heapify,heappop,heappush
n,m = map(int,input().split())
arr = list(map(int,input().split()))
heapify(arr)

for i in range(m):
    a = heappop(arr)
    b = heappop(arr)
    c = a+b
    heappush(arr,c)
    heappush(arr,c)

print(sum(arr))