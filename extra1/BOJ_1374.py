from collections import deque

n = int(input())

lectures = []
res = 1
for i in range(n):
    m, s,e = map(int,input().split())
    lectures.append((e,s))
lectures.sort()
print(lectures)
rooms = deque([lectures[0]])

for i in range(1,n):
    if lectures[i][1] < rooms[0][0]:
        res += 1
    else:
        rooms.popleft()
    rooms.append(lectures[i])

print(res)
