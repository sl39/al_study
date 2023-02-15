import sys
from collections import deque

input = sys.stdin.readline

N, D, K, C = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
numbers += numbers[:K-1]
counter = [ 0 for _ in range(D+1) ]

window = deque()
count = 0
answer = 0
for k, v in enumerate(numbers):
    window.append(v)
    counter[v] += 1
    if counter[v] == 1:
        count += 1

    if k < K - 1:
        continue

    if counter[C] == 0:
        answer = max(answer, count+1)
    else:
        answer = max(answer, count)

    p = window.popleft()
    counter[p] -= 1
    if counter[p] == 0:
        count -= 1

print(answer)