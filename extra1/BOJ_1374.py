from heapq import heappop,heappush

n = int(input())

lectures = []
for i in range(n):
    m, s,e = map(int,input().split())
    heappush(lectures,(s,e))

rooms= []
s,e = heappop(lectures)
heappush(rooms,e)
while lectures:
    s,e = heappop(lectures)
    if s >= rooms[0]:
        heappop(rooms)
    heappush(rooms,e)

print(len(rooms))
