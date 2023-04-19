
import sys
from heapq import heappop, heappush
input =sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    k = int(input())
    if k == 0:
        if not arr:
            print(0)
        else:
            a = heappop(arr)
            print(-a)
    else:
        heappush(arr,-k)